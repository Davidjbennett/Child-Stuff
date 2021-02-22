// string3.h: String implementation (Note: parameter names not required in declarations)

#ifndef STRING3_H
#define STRING3_H

#include <iosfwd>               // Just contains declarations (no bodies)

class String {
    char* data_ptr;             // Pointer to the dynamic array of chars
    char* init(const char*);    // Reallocate heap memory
public:
    String(const char* = "");
    String(const String&);
    ~String();
    String& operator=(const String&);
    friend String operator+(const String&, const String&);
    friend std::ostream& operator<<(std::ostream&, const String&);
};

#endif
