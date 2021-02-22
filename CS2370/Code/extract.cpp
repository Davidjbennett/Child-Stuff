#include <iostream>
using namespace std;

int main() {
    unsigned int n = 65534;             // 0b0000'0000'0000'0000'1111'1111'1111'1110
    unsigned int mask = 0xaaaaaaaa;     // 0b1010'1010'1010'1010'1010'1010'1010'1010
    cout << (n & mask) << endl;         // 0b0000'0000'0000'0000'1010'1010'1010'1010
}

/* Output:
43690
*/
