#include <iostream>

using namespace std;

int gcd(int p, int q) {
    if (q == 0) { return p; }
    int r = p % q;
    return gcd(q, r);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <num1> <num2>" << endl;
        return 1;
    }

    int num1 = stoi(argv[1]);
    int num2 = stoi(argv[2]);
    int result = gcd(num1, num2);
    
    cout << "The greated common divisor of " << num1 << " and " << num2 << " is " << result << endl;
}