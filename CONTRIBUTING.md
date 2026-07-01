# Contributing

This repo holds my personal problem sets and notes for CodePath's **TIP101** course, so it isn't a typical open-source project looking for contributors. That said, if we worked through a problem together in session and you've got a fixed or improved solution, I'd genuinely love to see it — sharing alternative approaches is one of the best ways to learn.

## Ways to contribute

- **Open an issue** if you spot a bug, a wrong problem statement, or an outdated note.
- **Open a pull request** if you have an alternative or improved solution to a problem.
- **Reach out directly** (Slack, LinkedIn, or email — see the README) if it's easier to just show me your version.
- **VS Code Live Share** — if we were (or are) in the same breakout room and I send you a Live Share link, anything you type or fix live counts as contributing too automatically! You don't need a PR for that, but feel free to open one afterward if you want it reflected here permanently.

## What I'm looking for

A working solution alone isn't enough — I want to actually understand it. So please also:

- **Explain why it works.** A sentence or two in the PR description (or a comment in the code) on the intuition/approach goes a long way.
- **Comment your code well.** Not line-by-line noise, but enough that I can follow the logic without having to reverse-engineer it.

## Fixing the problem files themselves

The `.md` and starter `.py` files are pulled from the CodePath course portal, and they're not always perfect. If you find a copy-paste error, a typo, a broken example, or a syntax mistake in either file, go ahead and fix it directly — you don't need to preserve it just because it came from the portal.

## Revisiting old or unfinished work

Feel free to go back through any of my old solutions, even in units we've already moved past. If we worked through a problem together in a session and never got the chance to fully finish it, pick it back up and finish it — I'd rather have a complete, correct solution than leave it half-done.

## Submitting a solution

1. Fork the repo and create a branch off `main`.
2. Find the problem's folder, e.g. `Unit 04/Session 2/Problem Set 1/`.
3. Edit the matching `.py` file (and the `.md` file too, if it has an error — see above).
4. Keep the existing function/method signatures so the file still matches the problem's stub and example calls.
5. Make sure your solution runs and passes the examples given in the `.md` file.
6. Open a PR describing what changed, why your approach works, and why it's better if you're improving on an existing solution.

## If you find a better approach

If you come up with a solution that's better than what's already there — say, smaller time or space complexity — **don't replace the old one.** Add your version alongside it (the same way `Problem 3: Valid Palindrome.py` already keeps `valid_palindrome1` and `valid_palindrome2` side by side), and add a comment explaining specifically why the new one is better (e.g. the old one is O(n²) because of repeated slicing, the new one is O(n) because it avoids that). I want to see the comparison, not just the winner.

## Testing your code

Follow the pattern already used in files like `Problem 3: Valid Palindrome.py`: define your test inputs, then add `print(...)` calls for each solution so the output is visible when the file is run in the terminal. If there are multiple solutions in the file, group each solution's print statements together (with a blank `print()` between groups) so I can visually compare that they produce the same output.

Also feel free to add extra test cases or print statements for edge cases the existing solution might have missed (empty input, single character, all-duplicate input, etc.) — surfacing an edge case I didn't consider is a contribution in itself.

## Style

- Solutions are written in Python.
- Prefer clear, idiomatic code over clever one-liners — this repo is for learning, not code golf.
- Comment for the "why," not just the "what" — explain the approach and any non-obvious tricks or invariants, not just what each line does.

## Code of conduct

Be kind, be constructive, and keep feedback focused on the code. This is a learning space.

## Contact

- 💬 **Slack** — Ping or direct message me in the course Slack! My profile name is Srihas Gupta
- 🔗 **LinkedIn** — [linkedin.com/in/srihas115](https://www.linkedin.com/in/srihas115/)
- 📧 **Email** - srihasgupta@gmail.com
