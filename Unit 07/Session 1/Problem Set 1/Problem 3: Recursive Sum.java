import java.util.List;
import java.util.Arrays;

/*
1. understand
    input: list
    output: sum of all values
    core logic: recursion

3. plan
    base case: if the list is empty, then return 0
    recursive step:
        return the value of the first element of the list + sumList(rest of the list)
*/

class RecursiveSum {

    // Time: O(n^2) because each of the n calls creates a new sublist via subList(1, size),
    //       and building that sublist takes O(k) time/space to copy for a list of length k —
    //       summing n + (n-1) + ... + 1 gives O(n^2) total work.
    // Space: O(n^2) because each call also holds a newly allocated sublist in
    //        memory until its call returns (sizes n-1, n-2, ..., 0), in addition
    //        to the O(n) call stack — the sublist copies dominate the total.
    public static int sumList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return 0;
        }
        int first = lst.get(0);
        List<Integer> rest = new java.util.ArrayList<>(lst.subList(1, lst.size())); // copies remaining elements
        return first + sumList(rest);
    }

    // Public-facing overload — matches the original single-argument signature
    public static int sumList2(List<Integer> lst) {
        return sumList2(lst, 0);
    }

    // Time: O(n) because i indexes into lst and increments once per call, and
    //       lst.get(i) is an O(1) lookup with no copying — n calls, O(1) work each.
    // Space: O(n) because the call stack grows one frame per call until the
    //        base case is hit, but no extra lists are ever created — just n
    //        stacked frames, each holding a reference to the same lst and an int.
    public static int sumList2(List<Integer> lst, int i) {
        if (i == lst.size()) {
            return 0;
        }
        return lst.get(i) + sumList2(lst, i + 1);
    }

    public static void main(String[] args) {
        // Example Input: [1, 2, 3, 4, 5]
        System.out.println(sumList(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(sumList(Arrays.asList(5)));
        System.out.println(sumList(Arrays.asList()));

        System.out.println();

        // No list copying
        System.out.println(sumList2(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(sumList2(Arrays.asList(5)));
        System.out.println(sumList2(Arrays.asList()));
    }
}