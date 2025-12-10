#include <iostream>
#include "my_dsa.h"

int main(int argc, char* argv[]) {
    // Validate arguments
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <num1> <num2>" << std::endl;
        return 1;
    }

    // Parse inputs into positive integers
    int num1 = std::stoi(argv[1]);
    int num2 = std::stoi(argv[2]);
    
    int gcd = my_dsa::euclids_algorithm(num1, num2);
    
    std::cout << "The greated common divisor of " << num1 << " and " << num2 << " is " << gcd << std::endl;

    return 0;
}