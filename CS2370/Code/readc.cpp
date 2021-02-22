// readc.cpp: Shows how to read and validate characters
#include <cctype>
#include <iostream>
using namespace std;

int main() {
    char c;

    do {
        cout << "Enter a character (q to quit): ";
        cin >> c;
        if (!isalpha(c)) {
            cout << "Please enter letters only\n";
            continue;
        }
        cout << "you entered " << c << endl;
        c = tolower(c);
    } while (c != 'q');
}
