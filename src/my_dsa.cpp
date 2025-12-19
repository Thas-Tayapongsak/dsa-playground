#include <cstdlib>
#include <vector>
#include <algorithm>
#include "my_dsa.h"

namespace my_dsa {
    int euclids_algorithm(int p, int q) {
        // Make negative integers positive
        p = std::abs(p);
        q = std::abs(q);

        // ALGORITHM
        if (q == 0) { return p; }
        int r = p % q;
        return euclids_algorithm(q, r);
    }

    int binary_search(int key, std::vector<int>& num_list) {
        return 0;
    }
}