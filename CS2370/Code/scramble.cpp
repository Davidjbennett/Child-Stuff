#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int level = -1;
void indent() {
    for (int i = 0; i < level; ++i)
        cout << "   ";
}

void permute(string s, int start) {
    ++level;
    indent();
    cout << "substring: " << s.substr(start) << endl;

    // Base case: we are at the last letter (nothing to do)
    const auto nchars = s.size();
    if (start == nchars-1)
        cout << "> " << s << endl;
    else {
        // Process starting from character at position "start"
        for (int i = start; i < nchars; ++i) {
            swap(s[start], s[i]);   // Move a character to the start position
            permute(s, start+1);    // Process rest recursively
            swap(s[start], s[i]);   // Backtrack (restore string to before the swap)
        }
    }
    --level;
}

void scramble(const string& s) {
    permute(s, 0);      // helper function
}

int main() {
    scramble("cat");
}

/* Output:
substring: cat
   substring: at              (c|at)
      substring: t            (ca|t)
> cat
      substring: a            (ct|a)
> cta
   substring: ct              (a|ct)
      substring: t            (ac|t)
> act
      substring: c            (at|c)
> atc
   substring: ac              (t|ac)
      substring: c            (ta|c)
> tac
      substring: a            (tc|a)
> tca
*/
