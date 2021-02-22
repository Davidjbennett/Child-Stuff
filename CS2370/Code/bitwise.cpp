// Illustrate bitwise ops
#include <iostream>
using namespace std;

int main() {
    unsigned int n = 0x0a0b0c0d;    // 0b0000'1010'0000'1011'0000'1100'0000'1101
    cout << hex;

    // Print each nybble left-to-right
    unsigned int mask = 0xf0000000;
    for (int i = 0; i < 8; ++i) {
        auto bits = mask & n;
        cout << (bits >> ((7-i)*4));
        mask >>= 4;
    }
    cout << endl;

    // Print each bit left-to-right after flipping n's bits
    mask = 0x80000000;
    n = ~n;
    for (int i = 0; i < 32; ++i) {
        auto bits = mask & n;
        cout << !!bits;     // The first ! gives 0 or 1, the second flips to 1 or 0
        mask >>= 1;
    }
    cout << endl;
}

/* Output:
0a0b0c0d
11110101111101001111001111110010
*/
