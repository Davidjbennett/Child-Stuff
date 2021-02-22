// Shows that local references are trivial aliases (no pointers used)
#include <iostream>
using namespace std;

int main() {
    int n = 10;
    int& r = n;
    r *= 2;
    cout << n << endl;
    cout << &n << ", " << &r << endl;
}

/* Output:
20
0x7ffee8a419fc, 0x7ffee8a419fc
*/
