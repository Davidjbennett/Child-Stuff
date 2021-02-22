// upper.cpp: Converts a string upper case.
//            Illustrates that toupper returns an int!
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "David";

    // First attempt: print letters as upper case
    for (char c: s)
        cout << toupper(c);
    cout << endl;

    // Fix: Cast to char
    for (char c: s)
        cout << char(toupper(c));
    cout << endl;
}

/* Output:
6865867368
DAVID
*/
