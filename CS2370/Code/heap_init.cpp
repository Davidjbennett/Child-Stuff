#include <iostream>
using namespace std;

class Foo {
public:
    Foo() {
        cout << "a Foo is born at " << static_cast<void*>(this) << endl;
    }
    ~Foo() {
        cout << "a Foo has died at " << static_cast<void*>(this) << endl;
    }
};

int main() {
    Foo* p1 = new Foo;  // new Foo(): parens optional here
    Foo* p2 = new Foo[5];

    // Commenting-out the following will print nothing and memory is not immediately freed.
    delete p1;
    delete [] p2;   // Brackets required. Try it without it.
}

/* Output:
a Foo is born at 0x7ff658c058e0
a Foo is born at 0x7ff658c058f8
a Foo is born at 0x7ff658c058f9
a Foo is born at 0x7ff658c058fa
a Foo is born at 0x7ff658c058fb
a Foo is born at 0x7ff658c058fc
a Foo has died at 0x7ff658c058e0
a Foo has died at 0x7ff658c058fc
a Foo has died at 0x7ff658c058fb
a Foo has died at 0x7ff658c058fa
a Foo has died at 0x7ff658c058f9
a Foo has died at 0x7ff658c058f8
*/
