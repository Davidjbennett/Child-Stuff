// init2.cpp: Shows how a default constructor is used by default.
//            In this example, both s and p are intialized twice.
//            You can't see that s is intialized twice, though. There 
//            is a trace print in Part's default ctor, however.

#include <iostream> 
#include <string>
using namespace std;

struct Part {
    int n;
    Part() {
        cout << "Executing Part()\n";
        n = 0;
    }
    Part(int n) {
        cout << "Executing Part(int)\n";
        this->n = n;
    }
    void display() const {
        cout << "n = " << n << endl;  
    }
};

struct Whole {
    string s;
    Part p;
    Whole(const string& s, const Part& p) {
        cout << "Running Whole's ctor\n";
        this->s = s;
        this->p = p;            // Assignment. Not a constructor call!
    }
    void display() const {
        cout << "s = " << s << " ";
        p.display();
    }
};

int main() {
    Part p(1);
    Whole w("one", p);
    w.display();
}

/* Output:
Executing Part(int)             ==> From line 40
Executing Part()                ==> Automatic as part of the Whole constructor!
Running Whole's ctor
s = one n = 1
*/
