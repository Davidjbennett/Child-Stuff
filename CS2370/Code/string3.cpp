// string3.cpp: Separate String implementation
#include "string3.h"
#include <cstring>
#include <iostream>   // Full definitions from stream library
using namespace std;

char* String::init(const char* from) {
    cout << "init from \"" << from << "\"\n";
    return strcpy(new char[strlen(from)+1], from);
}

String::String(const char* s) {     // Lose default argument!
    cout << "ctor\n";
    data_ptr = init(s);
}

String::String(const String& s) {   // Copy constructor
    cout << "copy ctor\n";
    data_ptr = init(s.data_ptr);
}

String::~String() {                 // Destructor
    cout << "dtor\n";
    delete [] data_ptr;
}

String& String::operator=(const String& s) { // Assignment operator
    if (this != &s) {                // Avoid self-assignment
        cout << "assign\n";
        char* new_data_ptr = init(s.data_ptr);
        delete [] data_ptr;          // Free old memory
        data_ptr = new_data_ptr;
    }
    return *this;                    // To allow s = t = w;
}

String operator+(const String& s1, const String& s2) {
    // Allocate and populate new memory for concatenation
    int len1 = strlen(s1.data_ptr);
    int new_len = len1 + strlen(s2.data_ptr) + 1;
    char* new_data_ptr = new char[new_len];
    strcpy(new_data_ptr, s1.data_ptr);
    strcat(new_data_ptr, s2.data_ptr);  // Concatenate s2 to s1

    // Prepare new result (Use default ctor to avoid needless copy)
    String result;
    delete [] result.data_ptr;       // Free old memory
    result.data_ptr = new_data_ptr;
    return result;
}

ostream& operator<<(ostream& os, const String& s) {
    return os << s.data_ptr;
}   
