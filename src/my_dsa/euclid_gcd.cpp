#include "my_dsa/euclid_gcd.h"

namespace my_dsa {
    int euclid_gcd(int p, int q) {
        if (q == 0) { return p; }
        int r = p % q;
        return euclid_gcd(q, r);
    }
}