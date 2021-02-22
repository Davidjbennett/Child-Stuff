/* xor.cpp: Shows the XOR swap trick (swaps without using temporary memory)
 *
 * Also shows that false prints as 0 and true as 1 by default
 */

#include <iostream>
using namespace std;

int main() {
    int n = 11, m = 5;
    m ^= n;
    n ^= m;
    m ^= n;
    cout << n << ' ' << m << endl;  // 5 11
    cout << endl;

    // Prove it works by cases
    for (auto b1: {false, true})
        for (auto b2: {false, true}) {
            bool x = b1;
            bool y = b2;

            x ^= y;
            y ^= x;
            x ^= y;
            cout << boolalpha;
            cout << "swapping " << b1 << " and " << b2 << " -> " << x << ' ' << y << endl;
            cout << noboolalpha;
            cout << "swapping " << b1 << " and " << b2 << " -> " << x << ' ' << y << endl;
            cout << endl;
        }
}

/* Output:
5 11

swapping false and false -> false false
swapping 0 and 0 -> 0 0

swapping false and true -> true false
swapping 0 and 1 -> 1 0

swapping true and false -> false true
swapping 1 and 0 -> 0 1

swapping true and true -> true true
swapping 1 and 1 -> 1 1
*/
