// unwind3.cpp: Illustrates unique_ptr, an object that wraps a pointer.
//              unique_ptr's destructor calls delete on its held pointer.
#include <iostream>
#include <memory>   // For unique_ptr
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
    unique_ptr<Foo> p(new Foo(2));
    throw runtime_error("I give up!");
}
void f() {
    unique_ptr<Foo> p(new Foo(1));
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
