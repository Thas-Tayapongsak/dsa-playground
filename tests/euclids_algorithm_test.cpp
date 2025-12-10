#include <gtest/gtest.h>
#include "my_dsa/euclids_algorithm.h"

TEST(EuclidsAlgorithm, HandlesPositiveNumbers) {
    EXPECT_EQ(my_dsa::euclids_algorithm(48, 18), 6);
    EXPECT_EQ(my_dsa::euclids_algorithm(101, 10), 1);
}

TEST(EuclidsAlgorithm, HandlesNegativeNumbers) {
    EXPECT_EQ(my_dsa::euclids_algorithm(-48, -18), 6);
    EXPECT_EQ(my_dsa::euclids_algorithm(-101, -10), 1);
}

TEST(EuclidsAlgorithm, HandlesMixedSignedNumbers) {
    EXPECT_EQ(my_dsa::euclids_algorithm(48, -18), 6);
    EXPECT_EQ(my_dsa::euclids_algorithm(-101, 10), 1);
}