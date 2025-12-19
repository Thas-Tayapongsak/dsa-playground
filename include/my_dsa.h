#pragma once
#include <vector>

namespace my_dsa {
    /**
     * @brief Computes the Greatest Common Divisor (GCD) of two integers.
     *
     * This function uses Euclid's Algorithm to determine the largest positive 
     * integer that divides both numbers without a remainder. 
     * 
     * @note Negative inputs are treated as their absolute values.
     *
     * @param p The first integer.
     * @param q The second integer.
     * @return The greatest common divisor of p and q.
     */
    int euclids_algorithm(int p, int q);

    /**
     * @brief Find the index of the key in the array using binary search algorithm. Return -1 if not found.
     * 
     * This function uses the binary search algorithm to determine if a given integer 
     * is a member of an array or not. It will sort the array, create an array of original indices, 
     * use binary search algorithm, access the original index, and return the found index.
     * If the key is not found, it will return -1.
     * 
     * @param key The integer to find.
     * @param num_list The array of integers.
     * @return The original index if found, or -1 if not found.
     */
    int binary_search(int key, std::vector<int>& num_list);
}
