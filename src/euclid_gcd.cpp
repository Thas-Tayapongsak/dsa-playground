#include "euclid_gcd.h"

int euclid_gcd(int p, int q) {
    if (q == 0) { return p; }
    int r = p % q;
    return euclid_gcd(q, r);
}