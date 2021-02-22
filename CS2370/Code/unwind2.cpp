// unwind2.cpp: Illustrates rhat raw pointers do not have destructors; only objects do.
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

// Functions g and f each have local pointers to a Foo object
void g() {
    Foo* pf = new Foo(2);
    throw runtime_error("I give up!");
    delete pf;   // Unreachable; but delete pf would call ~Foo() which runs delete p
}
void f() {
    Foo* pf = new Foo(1);
    g();
    delete pf;   // Unreachable; (ditto above)
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
I give up!
*/
