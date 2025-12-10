#pragma once

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
}
