#include <iostream>
#include <memory>
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
    int get_n() const {
       return n;
    }
    friend ostream& operator<<(ostream& os, const Foo& f) {
        return os << f.n;
    }
};

int main() {
    unique_ptr<Foo> p1(new Foo);  // new Foo(): parens optional here
    unique_ptr<Foo[]> p2(new Foo[5]);
    cout << p1->get_n() << endl;    // (*p1).get_n()
    // for (int i: {0,1,2,3,4})
    //     cout << &p2 << " holds a " << p2->get_n() << endl; // p2[i] == *(p2+i)

    // Commenting-out the following will print nothing and memory is not immediately freed.
    // delete p1;
    // delete [] p2;   // Brackets required. Try it without it.
}

/* Output:
a Foo is born at 0x7fad8ed04098
a Foo is born at 0x7fad8ed0409c
a Foo is born at 0x7fad8ed040a0
a Foo is born at 0x7fad8ed040a4
a Foo is born at 0x7fad8ed040a8
0
a Foo has died at 0x7fad8ed040a8
a Foo has died at 0x7fad8ed040a4
a Foo has died at 0x7fad8ed040a0
a Foo has died at 0x7fad8ed0409c
a Foo has died at 0x7fad8ed04098
a Foo has died at 0x7fad8ed04080
*/
