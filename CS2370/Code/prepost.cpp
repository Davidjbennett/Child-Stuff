#include <iostream>
using namespace std;

int main() {
    int x = 1;
    int z = x++;    // x is incremented after assigning to z
    int y = ++z;    // z is incremented before assigning to y
    int w = y--;    // y is incremented after assigning to w
    int v = --w;    // w is incremented before assigning to w
    cout << "x = " << x << endl;    // 2
    cout << "y = " << y << endl;    // 1
    cout << "z = " << z << endl;    // 2
    cout << "w = " << w << endl;    // 1
    cout << "v = " << v << endl;    // 1
}

/* Output:
x = 2
y = 1
z = 2
w = 1
v = 1
*/
