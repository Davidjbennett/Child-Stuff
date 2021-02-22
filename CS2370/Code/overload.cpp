#include <iostream>
#include <string>
using namespace std;

void display(int n) {
    cout << "Integer: " << n << ", occupies " << sizeof(int) << " bytes\n";
}

void display(const string& s) {
    cout << "String: \"" << s << "\" occupies " << sizeof(string)
         << " bytes on the stack, but has " << s.size() << " chars on the heap\n";
}

int main() {
    int n = 27;
    string s = "A stitch in time";
    display(n);
    display(s);
}
