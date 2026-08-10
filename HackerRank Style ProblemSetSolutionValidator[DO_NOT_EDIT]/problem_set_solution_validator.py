# ==============================================================================
#  PROBLEM SET SOLUTION VALIDATOR ENGINE  —  DO NOT EDIT  ·  DO NOT DELETE
# ==============================================================================
#  This file powers the problem set solution validator for every problem. It is shared by all
#  sessions and all courses. Editing or deleting it will break grading for
#  everyone. If something looks wrong, tell your instructor — do not change it.
#
#  Pure Python standard library only. No installation, no dependencies.
#  Runs on any machine with Python 3.8+.
# ==============================================================================

from __future__ import annotations

import ast
import atexit
import base64
import copy
import io
import json
import math
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

# ------------------------------------------------------------------------------
#  Terminal styling (degrades gracefully when the terminal has no color)
# ------------------------------------------------------------------------------

_COLOR = sys.stdout.isatty() and sys.platform != "emscripten"


def _c(text: str, code: str) -> str:
    if not _COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def _dim(t: str) -> str:
    return _c(t, "2")


def _bold(t: str) -> str:
    return _c(t, "1")


def _green(t: str) -> str:
    return _c(t, "32")


def _red(t: str) -> str:
    return _c(t, "31")


def _cyan(t: str) -> str:
    return _c(t, "36")


PASS_BOX = "✅"
FAIL_BOX = "❌"

_GRID_WIDTH = 5  # boxes per row


# ------------------------------------------------------------------------------
#  Value formatting & comparison
# ------------------------------------------------------------------------------

_FLOAT_TOL = 1e-9


def _is_number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def values_equal(a, b) -> bool:
    """Deep equality with float tolerance so 0.1+0.2 == 0.3 grades as correct."""
    if _is_number(a) and _is_number(b):
        return math.isclose(a, b, rel_tol=_FLOAT_TOL, abs_tol=_FLOAT_TOL)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if type(a) is not type(b) or len(a) != len(b):
            return False
        return all(values_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            return False
        return all(values_equal(a[k], b[k]) for k in a)
    return a == b


def fmt(value) -> str:
    """Render a value the way a student would recognize it."""
    from _viz import render_value  # linked lists / trees know how to draw themselves

    special = render_value(value)
    if special is not None:
        return special
    return repr(value)


def _fmt_call(func_name: str, args, kwargs) -> str:
    parts = [fmt(a) for a in args]
    parts += [f"{k}={fmt(v)}" for k, v in (kwargs or {}).items()]
    return f"{func_name}({', '.join(parts)})"


# ------------------------------------------------------------------------------
#  Running a single case
# ------------------------------------------------------------------------------

def _friendly_error(exc) -> str:
    """Turn common crashes into a plain-language hint. The most frequent student
    mistake is renaming something the problem set solution validator looks for (a class, a function, or
    a specifically-named variable), so we call that out by name."""
    name = type(exc).__name__
    msg = str(exc)
    m = re.search(r"name '([^']+)' is not defined", msg)
    if m:
        return (f"a NameError — the problem set solution validator couldn't find anything named "
                f"'{m.group(1)}'. Keep the class/function names the problem gives you, "
                f"and use the exact variable name it asks for (names are case-sensitive).")
    m = re.search(r"has no attribute '([^']+)'", msg)
    if m:
        return (f"an AttributeError — it tried to use .{m.group(1)}, but that wasn't "
                f"found. Check the attribute name matches the given class exactly.")
    if name == "TypeError" and "argument" in msg:
        return (f"a TypeError about arguments — {msg}. Make sure your function/method "
                f"keeps the exact parameters the problem's stub shows.")
    return f"{name}: {msg}"


class _Result:
    __slots__ = ("ok", "call", "expected", "got", "error", "mode", "detail", "kind")

    def __init__(self, ok, call, expected, got, error, mode, detail=None, kind="plain"):
        self.ok = ok
        self.call = call
        self.expected = expected
        self.got = got
        self.error = error
        self.mode = mode
        self.detail = detail  # overrides the default expected/got line when set
        self.kind = kind      # ret_kind for structure rendering (linkedlist/tree/plain)


def _run_case(func, args, kwargs, expected, mode, match="exact", predicate=None,
              arg_kinds=None, ret_kind="plain"):
    """mode: 'return' compares the return value, 'stdout' compares printed text,
    'inplace_length' compares (returned length, sorted prefix).
    match: 'exact', 'prefix_plus', 'unordered', or 'predicate'.
    arg_kinds/ret_kind: build linked lists / trees from array inputs and convert
    the return back to a canonical array before comparing."""
    from _structures import prepare_args, canon
    kwargs = kwargs or {}
    display_args = args
    built = prepare_args(args, arg_kinds) if arg_kinds else list(args)
    call = _fmt_call(getattr(func, "__name__", "solution"), display_args, kwargs)
    original = copy.deepcopy(built)   # kept for predicates (call may mutate args)
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            ret = func(*built, **kwargs)
    except Exception as exc:  # noqa: BLE001 — student code may raise anything
        return _Result(False, call, expected, None,
                       _friendly_error(exc), mode, kind=ret_kind)

    if match == "predicate":
        from _predicates import PREDICATES
        ok = bool(PREDICATES[predicate](list(original), ret))
        detail = None if ok else "your output isn't a valid arrangement for this problem"
        return _Result(ok, call, expected, ret, None, mode, detail)

    if mode == "inplace_length":
        k = ret
        prefix = sorted(built[0][:k]) if built and isinstance(k, int) else None
        got = [k, prefix]
        ok = values_equal(got, expected)
        return _Result(ok, call, expected, got, None, mode)

    if match == "prefix_plus":
        got = _norm_stdout(buf.getvalue())
        prefix = expected.get("prefix", "")
        min_extra = expected.get("min_extra", 1)
        hint = expected.get("hint", "add a bit more text!")
        ok = got.startswith(prefix) and len(got.strip()) >= len(prefix) + min_extra
        detail = None if ok else hint
        return _Result(ok, call, expected, got, None, mode, detail)

    if mode == "stdout":
        got = buf.getvalue()
        ok = _norm_stdout(got) == _norm_stdout(expected)
        return _Result(ok, call, expected, got, None, mode)

    if mode == "mutates_arg0":
        # function returns nothing useful; grade the first argument it mutates.
        # ret_kind lets us canonicalize a mutated linked list / tree into an array.
        raw = built[0] if built else None
        got = canon(raw, ret_kind)
        ok = values_equal(got, expected)
        return _Result(ok, call, expected, got, None, mode, kind=ret_kind)

    got = canon(ret, ret_kind)
    if match == "unordered":
        # order doesn't matter (e.g. "return the indices in any order")
        try:
            ok = sorted(got) == sorted(expected)
        except TypeError:
            ok = values_equal(got, expected)
    else:
        ok = values_equal(got, expected)
    return _Result(ok, call, expected, got, None, mode, kind=ret_kind)


def _norm_stdout(s) -> str:
    s = "" if s is None else str(s)
    lines = [ln.rstrip() for ln in s.rstrip("\n").split("\n")]
    return "\n".join(lines)


def _decode_expected(case):
    """Expected answers ship base64-encoded so students can't read them out of
    the test-pack JSON. `e` holds base64(repr(value)); we read it back with
    ast.literal_eval (safe — literals only), which preserves int dict-keys,
    tuples, and exact floats. A plain `expected` key is honored for debugging."""
    if "e" in case:
        raw = base64.b64decode(case["e"].encode("ascii")).decode("utf-8")
        return ast.literal_eval(raw)
    return case.get("expected")


def _decode_args(case):
    args = case.get("args", [])
    return ast.literal_eval(args) if isinstance(args, str) else args


# ------------------------------------------------------------------------------
#  Rendering the report
# ------------------------------------------------------------------------------

def _grid(results) -> str:
    rows = []
    for i in range(0, len(results), _GRID_WIDTH):
        chunk = results[i:i + _GRID_WIDTH]
        rows.append("  " + " ".join(PASS_BOX if r.ok else FAIL_BOX for r in chunk))
    return "\n".join(rows)


def _score_emoji(passed, total) -> str:
    if total == 0:
        return "❔"
    if passed == total:
        return "🎉"
    return "🔧"   # anything short of a perfect score


def _fmt_expected_got(r) -> str:
    if r.detail is not None:
        return _red(r.detail)
    kind = getattr(r, "kind", "plain")
    if kind in ("linkedlist", "tree", "doubly", "keytree"):
        # render structures on their own lines for readability
        from _structures import render_canon
        exp = render_canon(r.expected, kind)
        if r.error is not None:
            return f"expected {_green(exp)}\n        but your code raised {_red(r.error)}"
        got = render_canon(r.got, kind)
        joiner = "\n        " if ("\n" in exp or "\n" in got) else "   "
        return f"expected {_green(exp)}{joiner}got {_red(got)}"
    if r.error is not None:
        return f"expected {_short(r.expected, r.mode)}, but your code raised {_red(r.error)}"
    return (f"expected {_green(_short(r.expected, r.mode))}, "
            f"got {_red(_short(r.got, r.mode))}")


def _short(value, mode, limit=60) -> str:
    if mode == "stdout":
        text = _norm_stdout(value).replace("\n", "⏎")
        text = f'"{text}"'
    else:
        text = fmt(value)
    if len(text) > limit:
        text = text[: limit - 1] + "…"
    return text


def _print_report(title_line, subtitle, results, section_label=None):
    passed = sum(1 for r in results if r.ok)
    total = len(results)
    out = []
    if section_label:
        out.append("")
        out.append(_bold(_cyan(section_label)))
    else:
        out.append("")
        out.append(_bold(f"Problem Set Solution Validator Results: {passed}/{total}  {_score_emoji(passed, total)}"))
        out.append(_dim(title_line) if title_line else "")
    if subtitle:
        out.append(_dim(subtitle))
    out.append("")
    out.append(_grid(results))
    fails = [r for r in results if not r.ok]
    if fails:
        out.append("")
        for idx, r in enumerate(results, start=1):
            if not r.ok:
                # No leading ❌ here — the grid above already shows each case's
                # status, so repeating it per line just doubles the emoji.
                out.append(f"  Test {idx}:  {r.call}")
                out.append(f"        {_fmt_expected_got(r)}")
    print("\n".join(out))
    _mark_graded()


# ------------------------------------------------------------------------------
#  Locating the test pack for the calling student file
# ------------------------------------------------------------------------------

_UNIT_RE = re.compile(r"[Uu]nit[ _]?0*(\d+)")
_SESSION_RE = re.compile(r"[Ss]ession[ _]?0*(\d+)")
_VERSION_RE = re.compile(r"[Vv]ersion[ _]?0*(\d+)")
_PROBLEM_RE = re.compile(r"0*(\d+)")  # leading number of the file name, e.g. 04_sum.py


def _packs_dir() -> Path:
    return Path(__file__).resolve().parent / "testpacks"


def _caller_frame_info():
    """Find the student file that called grade()/check_setup() by walking the call
    stack out of this engine module. Returns (Path, that frame's globals) so we can
    both locate the test pack AND read the student's own classes/variables."""
    this = Path(__file__).resolve()
    f = sys._getframe(1)
    while f is not None:
        fn = f.f_globals.get("__file__")
        if fn:
            try:
                if Path(fn).resolve() != this:
                    return Path(fn).resolve(), f.f_globals
            except OSError:
                pass
        f = f.f_back
    return None, {}


def _caller_file(func) -> Path | None:
    f = getattr(func, "__globals__", {}).get("__file__")
    return Path(f).resolve() if f else None


def _locate_path(caller: Path):
    """Identify (unit, session, version, problem) from the calling file's PATH.

    The path fully determines which problem this is, e.g.
        .../Unit 01 - Python & Lists/Session 1/Version 1/04_sum.py
    so two problems that happen to use the same function name never collide.
    A combined file like `03_to_05_pokemon.py` keys off its leading number (03).
    """
    path_str = str(caller)
    um = _UNIT_RE.search(path_str)
    sm = _SESSION_RE.search(path_str)
    vm = _VERSION_RE.search(path_str)
    pm = _PROBLEM_RE.match(caller.name)
    if not (um and sm and vm and pm):
        raise ProblemSetSolutionValidatorError(
            "Could not tell which Unit / Session / Version / Problem this file is.\n"
            f"      File: {caller}\n"
            "      Expected a path like .../Unit 01 .../Session 1/Version 1/04_name.py")
    return int(um.group(1)), int(sm.group(1)), int(vm.group(1)), int(pm.group(1))


def _load_problem_for_file(caller: Path):
    unit, session, version, number = _locate_path(caller)
    key = f"unit{unit:02d}_session{session}"
    pack_path = _packs_dir() / f"{key}.json"
    if not pack_path.exists():
        raise ProblemSetSolutionValidatorError(f"No test pack found for {key} (looked in {pack_path}).")
    with open(pack_path, encoding="utf-8") as fh:
        pack = json.load(fh)
    pid = f"v{version}_p{number:02d}"
    problem = pack["problems"].get(pid)
    if problem is None:
        raise ProblemSetSolutionValidatorError(f"No test pack entry '{pid}' in {pack_path.name}.")
    return problem, pid


def _load_problem(func):
    caller = _caller_file(func)
    if caller is None:
        raise ProblemSetSolutionValidatorError("Could not determine which file called grade().")
    return _load_problem_for_file(caller)


class ProblemSetSolutionValidatorError(Exception):
    pass


# ------------------------------------------------------------------------------
#  Public API
# ------------------------------------------------------------------------------

def grade(obj=None):
    """Grade the current problem against its official test pack and print a report.

    Pass the function you wrote (function problems) or the class you completed
    (OOP problems). Setup/warm-up problems can just call check_setup()."""
    caller_file, caller_ns = _caller_frame_info()
    if caller_file is None:
        print(_red("\n⚠️  Problem Set Solution Validator could not determine which file called it."))
        return
    try:
        problem, _ = _load_problem_for_file(caller_file)
    except ProblemSetSolutionValidatorError as e:
        print(_red(f"\n⚠️  Problem Set Solution Validator could not run:\n      {e}"))
        return

    mode = problem.get("mode", "return")
    if mode == "scenario":
        _grade_scenario(problem, caller_ns, obj)
        return

    func = obj
    if func is None:
        print(_red("\n⚠️  grade() needs the function you wrote, e.g. grade(my_function)."))
        return
    global _graded_func
    _graded_func = func
    expected_name = problem.get("function")
    if expected_name and getattr(func, "__name__", None) != expected_name:
        print(_red(
            f"\n⚠️  This problem expects a function named '{expected_name}', "
            f"but you passed '{func.__name__}'.\n"
            "      Rename your function (and the grade(...) call) to match."))
        return

    match = problem.get("match", "exact")
    predicate = problem.get("predicate")
    arg_kinds = problem.get("arg_kinds")
    ret_kind = problem.get("ret_kind", "plain")
    cases = [c for c in problem["cases"] if not c.get("skip")]
    results = [
        _run_case(func, _decode_args(case), case.get("kwargs"),
                  _decode_expected(case), mode, match, predicate, arg_kinds, ret_kind)
        for case in cases
    ]
    title = problem.get("title", func.__name__)
    subtitle = f"{func.__name__}()"
    _print_report(title, subtitle, results)


def check_setup():
    """Grade a setup / warm-up problem: the problem set solution validator inspects the variables you
    created (using the exact names the problem specifies)."""
    grade(None)


# ------------------------------------------------------------------------------
#  Scenario grading (OOP methods, functions on objects, setup checks)
# ------------------------------------------------------------------------------

def _decode_code(case) -> str:
    return base64.b64decode(case["code"].encode("ascii")).decode("utf-8")


def _run_scenario_case(namespace, code, observe, expected, label):
    """Exec an authored scenario snippet against a COPY of the student's namespace
    (their classes / functions / variables). The snippet either assigns to RESULT
    (value check) or prints (stdout check)."""
    ns = dict(namespace)
    ns["RESULT"] = _SENTINEL
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            exec(code, ns)  # noqa: S102 — authored by the instructor, shipped in the pack
    except Exception as exc:  # noqa: BLE001
        return _Result(False, label, expected, None, _friendly_error(exc), observe)
    if observe == "stdout":
        got = _norm_stdout(buf.getvalue())
        ok = got == _norm_stdout(expected)
        return _Result(ok, label, expected, got, None, "stdout")
    got = ns.get("RESULT")
    if got is _SENTINEL:
        got = None
    ok = values_equal(got, expected)
    return _Result(ok, label, expected, got, None, "return")


def _grade_scenario(problem, caller_ns, obj):
    entry = problem.get("function")
    if entry and obj is not None and getattr(obj, "__name__", None) != entry:
        print(_red(
            f"\n⚠️  This problem expects something named '{entry}', "
            f"but you passed '{getattr(obj, '__name__', obj)}'."))
        return
    cases = [c for c in problem["cases"] if not c.get("skip")]
    results = []
    for case in cases:
        results.append(_run_scenario_case(
            caller_ns, _decode_code(case), case.get("observe", "return"),
            _decode_expected(case), case.get("label", "scenario")))
    title = problem.get("title", entry or "")
    subtitle = f"{entry}" if entry else ""
    _print_report(title, subtitle, results)


# --- student-authored custom tests -------------------------------------------

_SENTINEL = object()
_user_tests = []
_exit_registered = False
_graded = False
_graded_func = None


def _ensure_exit_hook():
    global _exit_registered
    if not _exit_registered:
        atexit.register(_at_exit)
        _exit_registered = True


def _mark_graded():
    """Called after a real grading run so the exit hook knows a student graded
    something (and can remind them to add their own tests if they didn't)."""
    global _graded
    _graded = True
    _ensure_exit_hook()


def _at_exit():
    # If the student wrote their own tests, show them. If they graded but wrote
    # none, nudge them to add some.
    if _user_tests:
        _flush_user_tests()
    elif _graded:
        print("\n" + _dim(
            "Reminder: Try coming up with your own custom test cases "
            "at the bottom of the file!"))


def test(func, *args, expected=_SENTINEL, mode=None, **kwargs):
    """Run YOUR OWN test case.

        test(product, 3, 4, expected=12)    -> checks against your own answer

    All your custom tests are collected and shown together under
    'Your Test Cases' after the official results.
    """
    global _graded_func
    if not callable(func):
        if _graded_func is not None:
            args = (func,) + args
            func = _graded_func
        else:
            raise ProblemSetSolutionValidatorError(
                "test() first argument must be callable, or a function must be graded first."
            )

    # Match the official grading style of this problem (so custom tests on a
    # print-based problem show the PRINTED output, not the return value).
    resolved_mode = mode
    arg_kinds = None
    ret_kind = "plain"
    match = "exact"
    predicate = None
    if resolved_mode is None:
        try:
            problem, _ = _load_problem(func)
            resolved_mode = problem.get("mode", "return")
            arg_kinds = problem.get("arg_kinds")
            ret_kind = problem.get("ret_kind", "plain")
            match = problem.get("match", "exact")
            predicate = problem.get("predicate")
        except ProblemSetSolutionValidatorError:
            resolved_mode = "return"
    # A student's own `expected` is always an exact comparison.
    if expected is _SENTINEL:
        # No expected value given: just run it and show the output (pass = it ran).
        r = _run_case(func, args, kwargs, _SENTINEL, resolved_mode, match, predicate, arg_kinds, ret_kind)
        if r.error is None:
            r.ok = True  # it executed without crashing
    else:
        r = _run_case(func, args, kwargs, expected, resolved_mode, match, predicate, arg_kinds, ret_kind)
    _user_tests.append(r)
    _ensure_exit_hook()


def _flush_user_tests():
    if not _user_tests:
        return
    # The grid above already shows each case's status, so the per-line detail
    # doesn't repeat the ✅/❌ (keeps it clean — no double emoji per test).
    out = ["", _bold(_cyan("Your Test Cases:")), ""]
    out.append(_grid(_user_tests))
    out.append("")
    for idx, r in enumerate(_user_tests, start=1):
        if r.error is not None:
            out.append(f"  Test {idx}:  {r.call}")
            out.append(f"        your code raised {_red(r.error)}")
        elif r.expected is _SENTINEL:
            out.append(f"  Test {idx}:  {r.call}  →  {_cyan(_short(r.got, r.mode))}")
        elif not r.ok:
            out.append(f"  Test {idx}:  {r.call}")
            out.append(f"        {_fmt_expected_got(r)}")
        else:
            out.append(f"  Test {idx}:  {r.call}  →  {_green(_short(r.got, r.mode))}")
    print("\n".join(out))


# Make `_viz` importable whether the engine is imported flat or as part of a pkg.
sys.path.insert(0, str(Path(__file__).resolve().parent))
