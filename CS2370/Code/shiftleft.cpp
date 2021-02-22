#include <bitset>
#include <iostream>
using namespace std;

int main() {
    signed char x = -127;
    cout << (x << 1) << endl;

    bitset<8> b(x);
    cout << b << endl;
    signed char y = x << 1;
    bitset<8> b2(y);
    cout << b2 << endl;
    bitset<32> b3(-127);
    cout << b3 << endl;
}