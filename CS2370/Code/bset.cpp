#include <bitset>
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Obtain an input string of letters
    string s;
    cout << "Enter a string with lowercase English letters (no spaces): ";
    cin >> s;

    // Construct the "set"
    unsigned int theSet = 0;
    for (char c: s) {
        int index = c - 'a';           // Find the letter's offset from 'a'
        if (0 <= index && index < 26)  // Ignore non-lowercase letters
            theSet |= (1 << index);    // Set the letter's corresponding bit
    }

    // Print theSet's bits
    cout << bitset<8*sizeof(unsigned int)>(theSet) << endl;
}