#include <iostream>
#include <vector>

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

// Time: O(n^2) because each of the n calls constructs a new vector from
//       lst.begin()+1 to lst.end(), and building that vector takes O(k) time/space
//       to copy for a vector of length k — summing n + (n-1) + ... + 1 gives O(n^2) total work.
// Space: O(n^2) because each call also holds a newly allocated vector in
//        memory until its call returns (sizes n-1, n-2, ..., 0), in addition
//        to the O(n) call stack — the vector copies dominate the total.
int sumList(std::vector<int> lst) {
    if (lst.empty()) {
        return 0;
    }
    int first = lst[0];
    std::vector<int> rest(lst.begin() + 1, lst.end()); // copies remaining elements
    return first + sumList(rest);
}

// Time: O(n) because i indexes into lst and increments once per call, and
//       lst[i] is an O(1) lookup with no copying — n calls, O(1) work each.
// Space: O(n) because the call stack grows one frame per call until the
//        base case is hit, but no extra vectors are ever created — just n
//        stacked frames, each holding a reference to the same lst and an int.
// lst is passed by const reference so it is never copied on any call.
int sumList2(const std::vector<int>& lst, int i = 0) {
    if (i == static_cast<int>(lst.size())) {
        return 0;
    }
    return lst[i] + sumList2(lst, i + 1);
}

int main() {
    // Example Input: {1, 2, 3, 4, 5}
    std::cout << sumList({1, 2, 3, 4, 5}) << std::endl;
    std::cout << sumList({5}) << std::endl;
    std::cout << sumList({}) << std::endl;

    std::cout << std::endl;

    // No vector copying
    std::cout << sumList2({1, 2, 3, 4, 5}) << std::endl;
    std::cout << sumList2({5}) << std::endl;
    std::cout << sumList2({}) << std::endl;

    return 0;
}