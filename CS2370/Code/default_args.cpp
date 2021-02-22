#include <cassert>
#include <iostream>
#include <string>
using namespace std;

char digit_chars[] = {'0','1','2','3','4','5','6','7',
                      '8','9','A','B','C','D','E','F'};

string convert(int num, int base = 10) {
    assert(2 <= base && base <= 16);

    string result;
    while (num > 0) {
        int digit = num % base;
        result = digit_chars[digit] + result;
        num /= base;
    }
    return result;
}

int main() {
    cout << convert(30, 2) << endl;     // Binary
    cout << convert(30) << endl;        // Decimal (default)
    cout << convert(30, 16) << endl;    // Hexadecimal
}