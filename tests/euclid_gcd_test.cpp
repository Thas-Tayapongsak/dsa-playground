#include <gtest/gtest.h>
#include "my_dsa/euclid_gcd.h"

TEST(EuclidGCD, HandlesPositiveNumbers) {
    EXPECT_EQ(my_dsa::euclid_gcd(48, 18), 6);
    EXPECT_EQ(my_dsa::euclid_gcd(101, 10), 1);
}