#include <algorithm>
#include <iostream>
#include <string>
using namespace std;


void permute(string s, int start) {
    // Base case: we are at the last letter (nothing to do)
    const auto nchars = s.size();
    if (start == nchars-1)
        cout << s << endl;  // Print this permutation
    else {
        // Process starting from character at position "start"
        for (int i = start; i < nchars; ++i) {
            swap(s[start], s[i]);   // Move a character to the start position
            permute(s, start+1);    // Process rest recursively
            swap(s[start], s[i]);   // Backtrack (restore string to before the swap)
        }
    }
}

void scramble(const string& s) {
    permute(s, 0);      // helper function
}

int main() {
    scramble("cat");
}

/* Output:
cat
cta
act
atc
tac
tca
*/
