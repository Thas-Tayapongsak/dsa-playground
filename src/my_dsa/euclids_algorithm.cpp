#include <cstdlib>
#include "my_dsa/euclids_algorithm.h"

namespace my_dsa {
    int euclids_algorithm(int p, int q) {
        // Validate and sanitize inputs
        p = std::abs(p);
        q = std::abs(q);

        // ALGORITHM
        if (q == 0) { return p; }
        int r = p % q;
        return euclids_algorithm(q, r);
    }
}