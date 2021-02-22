// Shows how integers wrap when overflowing

#include <climits>
#include <iostream>
using namespace std;

int main() {
    signed int n = INT_MAX;
    cout << n << endl;
    cout << n+1 << endl;

    unsigned int m = UINT_MAX;
    cout << m << endl;
    cout << m+1 << endl;
}

/* Output:
2147483647
-2147483648
4294967295
0
*/