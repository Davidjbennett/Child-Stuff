// inspect.cpp: Displays the bytes of any value
#include <cstddef>  // for size_t
#include <iostream>
using namespace std;

void inspect(const void* p, size_t size) {
    // Cast p to a byte*
    const byte* pb = static_cast<const byte*>(p);   // Look at bytes at address p
    cout << hex;
    for (size_t i = 0; i < size; ++i)
        cout << "0x" << int(pb[i]) << endl; // pb[i] == *(pb+i)
    cout << dec;
}

int main() {
    char c = 'a';
    inspect(&c, sizeof(c));
    int n = 7; // 000000000...000111 = 0007
    inspect(&n, sizeof(n));
    double x = 100.0;
    inspect(&x, sizeof(x));
    int two[] = {1,2};
    inspect(two, sizeof(two));
}
