#include <iostream>
#include "my_dsa/euclid_gcd.h"

using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <num1> <num2>" << endl;
        return 1;
    }

    int num1 = stoi(argv[1]);
    int num2 = stoi(argv[2]);
    int result = my_dsa::euclid_gcd(num1, num2);
    
    cout << "The greated common divisor of " << num1 << " and " << num2 << " is " << result << endl;
}