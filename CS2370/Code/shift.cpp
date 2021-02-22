#include <iostream>
using namespace std;

int main() {
    auto x = byte(0b00101101);      // 32+8+4+1 = 45
    cout << int(x << 1) << endl;    // 01011010 = 64+16+8+2 = 90
    cout << int(x << 2) << endl;    // 10110100 = 128+32+16+4 = 180
    cout << int(x << 4) << endl;    // 11010000 = 128+64+16 = 208
    cout << int(x << 8) << endl;    // 00000000 = 0
    cout << int(x >> 1) << endl;    // 00010110 = 16+4+2 = 22
    cout << int(x >> 4) << endl;    // 00000010 = 2
    cout << int(x >> 8) << endl;    // 00000000 = 0

    signed char y = 0b10101101;
    cout << int(y) << endl;         // 10101101 => 01010010+1 = 01010011 = 64+16+2+1 => -83
    cout << int(y >> 1) << endl;    // 11010110 => 00101001+1 = 00101010 = 32+8+2 => -42
    cout << int(y >> 4) << endl;    // 11111010 => 00000101+1 = 00000110 = 4+2 => -6  
    cout << int(y >> 8) << endl;    // 11111111 => 00000000+1 = 00000001 => -1

    unsigned int n = 45;
    unsigned int mask = 1 << 5;
    cout << (n & mask) << endl;     // 32 = 000...100000
    n |= (1 << 4);
    cout << n << endl;              // 61 = 000...111101
    n &= ~(1 << 4);
    cout << n << endl;              // 45 = 000...101101
}

/* Output:
90
208
0
22
2
0
-83
-42
-6
-1
32
61
45
*/
