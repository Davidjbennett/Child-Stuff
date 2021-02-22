#include <iostream>
using namespace std;

int main() {
    // Inspect an int
    int n = 1;
    byte* p = reinterpret_cast<byte*>(&n);
    for (int i = 0; i < sizeof(n); ++i)
        cout << int(p[i]) << ' ';
    cout << endl;

    // Inspect a struct
    struct Nums {
        int n;
        char s[4];
    };
    Nums nums = {16, "abc"};
    p = reinterpret_cast<byte*>(&nums);
    cout << hex;
    for (int i = 0; i < sizeof(nums); ++i)
        cout << int(p[i]) << ' ';
    cout << endl;
}

/* Output:
1 0 0 0
10 0 0 0 61 62 63 0 
*/
