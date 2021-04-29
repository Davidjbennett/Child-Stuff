// string.cpp: A String implementation
//             Trace statments announce every function invocation.
//             There is a *delete* for every *new* (via destructors)
//   
//   TODO: Combine the first 2 constructors.
//             
#include <cassert>
#include <cstddef>  // For size_t
#include <cstring>
#include <iostream>   
using namespace std;

class String {
    char* data_ptr;
    String(char* ptr, bool) {
        data_ptr = ptr;
    }
public:
    String() {
        cout << "default ctor\n";
        data_ptr = new char[1];          // For the '\0'
        assert(data_ptr);
        data_ptr[0] = '\0';
    }
    String(const char* s) {
        cout << "char* ctor\n";
        data_ptr = new char[strlen(s) + 1];    // Extra byte for '\0'
        assert(data_ptr);
        strcpy(data_ptr, s);
    }
    String(const String& s) {            // Copy constructor
        cout << "copy ctor\n";
        data_ptr = new char[strlen(s.data_ptr) + 1];
        assert(data_ptr);
        strcpy(data_ptr, s.data_ptr);
    }
    ~String() {                          // Destructor
        cout << "dtor\n";
        delete [] data_ptr;
    }
    String& operator=(const String& s) { // Assignment operator
        cout << "assign\n";
        if (&s != this) {
            char* new_data_ptr = new char[strlen(s.data_ptr) + 1];
            assert(data_ptr);
            strcpy(new_data_ptr, s.data_ptr);
            delete [] data_ptr;              // Free old memory
            data_ptr = new_data_ptr;
        }
        return *this;                    // To allow s = t = w;
    }
    size_t size() const {
        return strlen(data_ptr);
    }
    friend String operator+(const String& s1, const String& s2) {
        // Allocate and populate new memory for concatenation
        cout << "operator+\n";
        size_t new_len = strlen(s1.data_ptr) + strlen(s2.data_ptr) + 1;
        char* new_data_ptr = new char[new_len];
        assert(new_data_ptr);
        strcpy(new_data_ptr, s1.data_ptr);
        strcat(new_data_ptr, s2.data_ptr);  // Concatenate s2 to s1

        // Prepare new result (avoid needless copy)
        return String(new_data_ptr, false);
    }
    friend ostream& operator<<(ostream& os, const String& s) {
        return os << s.data_ptr;
    }
};

int main() {
    String s0;
    cout << "s0.size() == " << s0.size() << endl;
    String s("hello");
    String t("there");
    cout << s + " " + t << endl;    // (s + " ") + t = s.operator+(String(" ")).operator+(t)
    String w = "Hey " + t;          // String("Hey ") + t; 
    cout << w << endl;
    w = s = t;                      // w = (s = t);
    cout << s << endl;
    cout << t << endl;
    cout << w << endl;
}

/* Output:
default ctor
s0.size() == 0
char* ctor
char* ctor
char* ctor
operator+
operator+
hello there
dtor
dtor
dtor
char* ctor
operator+
dtor
Hey there
dtor
dtor
dtor
dtor
*/
