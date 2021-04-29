#include <iostream>
using namespace std;

class Foo {
    int n = 0;
public:
    Foo() {
        cout << "a Foo is born at " << static_cast<void*>(this) << endl;
    }
    ~Foo() {
        cout << "a Foo has died at " << static_cast<void*>(this) << endl;
    }
    friend ostream& operator<<(ostream& os, const Foo& f) {
        return os << f.n;
    }
};

int main() {
    Foo* p1 = new Foo;  // new Foo(): parens optional here
    Foo* p2 = new Foo[5];
    for (int i: {0,1,2,3,4})
        cout << p2 + i << " holds a " << p2[i] << endl; // p2[i] == *(p2+i)

    // Commenting-out the following will print nothing and memory is not immediately freed.
    delete p1;
    delete [] p2;   // Brackets required. Try it without it.
}

/* Output:
a Foo is born at 0x7f8b63405aa0
a Foo is born at 0x7f8b63405ab8
a Foo is born at 0x7f8b63405abc
a Foo is born at 0x7f8b63405ac0
a Foo is born at 0x7f8b63405ac4
a Foo is born at 0x7f8b63405ac8
0x7f8b63405ab8 holds a 0
0x7f8b63405abc holds a 0
0x7f8b63405ac0 holds a 0
0x7f8b63405ac4 holds a 0
0x7f8b63405ac8 holds a 0
a Foo has died at 0x7f8b63405aa0
a Foo has died at 0x7f8b63405ac8
a Foo has died at 0x7f8b63405ac4
a Foo has died at 0x7f8b63405ac0
a Foo has died at 0x7f8b63405abc
a Foo has died at 0x7f8b63405ab8
*/
