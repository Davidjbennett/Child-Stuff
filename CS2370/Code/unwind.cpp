// unwind.cpp: Illustrates stack unwinding
#include <iostream>
#include <stdexcept>
using namespace std;

class Foo {
    int* p;
public:
    Foo(int x) {
        p = new int(x);   // Allocate heap memory
        cout << *p << " allocated\n";
    }
    ~Foo() {
        cout << *p << " deallocated\n";
        delete p;
    }
};

// Functions g and f each have a local Foo object, which has a destructor.
void g() {
    Foo b(2);
    throw runtime_error("I give up!");
    cout << "g\n";  // Won't print
}
void f() {
    Foo a(1);
    g();
}

int main() {
    try {
        f();
        cout << "This won't print\n";
    }
    catch(runtime_error& exc) {
        cout << exc.what() << endl;
    }
}

/* Output:
1 allocated
2 allocated
2 deallocated
1 deallocated
I give up!
*/
