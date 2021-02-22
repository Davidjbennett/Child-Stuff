#include <iostream>
using namespace std;

int main() {
    auto x = byte(0b00101101);      // 45
    cout << int(x) << endl;
    auto y = byte(0b01101010);      // 106
    cout << int(y) << endl;
    cout << int(x | y) << endl;     // 01101111 = 64+32+8+4+2+1 = 111
    cout << int(x & y) << endl;     // 00101000 = 32+8 =40
    cout << int(x ^ y) << endl;     // 01000111 = 64+4+2+1 = 71

    cout << int(~x) << endl;        // 11010010 = 128+64+16+2 = 210
}

/* Output:
45
106
111
40
71
210
*/