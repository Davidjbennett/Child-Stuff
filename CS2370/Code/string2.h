// string.cpp: String implementation

#ifndef STRING_H
#define STRING_H

#include <iosfwd>           // Just contains declarations (no bodies)

class String {
    enum {CHUNK = 10};
    char* data_ptr;         // Pointer to the dynamic array of chars
    void grow();            // Reallocate to accommodate more chars
public:
    String(const char* s = "");
    String(const String& s);
    ~String();
    String& operator=(const String& s);
    friend std::ostream& operator<<(std::ostream& os, const String& s);
};

#endif
