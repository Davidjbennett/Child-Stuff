#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int level = -1;
void trace(const string& s, int start, int i) {
    // Indent
    for (int i = 0; i < level; ++i)
        cout << "   ";

    // Trace
    cout << "s = " << s << ", start = " << start << ", i = " << i << endl;
}

void permute(string s, int start) {
    ++level;

    // Base case: we are at the last letter (nothing to do)
    const auto nchars = s.size();
    if (start == nchars-1)
        cout << ">>> " << s << endl;
    else {
        // Process starting from character at position "start"
        for (int i = start; i < nchars; ++i) {
            trace(s, start, i);
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
    scramble("a"); cout << endl;
    scramble("be"); cout << endl;
    scramble("cat"); cout << endl;
    scramble("hear");
}

/* Output:
>>> a

s = be, start = 0, i = 0
>>> be
s = be, start = 0, i = 1
>>> eb

s = cat, start = 0, i = 0
   s = cat, start = 1, i = 1
>>> cat
   s = cat, start = 1, i = 2
>>> cta
s = cat, start = 0, i = 1
   s = act, start = 1, i = 1
>>> act
   s = act, start = 1, i = 2
>>> atc
s = cat, start = 0, i = 2
   s = tac, start = 1, i = 1
>>> tac
   s = tac, start = 1, i = 2
>>> tca

s = hear, start = 0, i = 0
   s = hear, start = 1, i = 1
      s = hear, start = 2, i = 2
>>> hear
      s = hear, start = 2, i = 3
>>> hera
   s = hear, start = 1, i = 2
      s = haer, start = 2, i = 2
>>> haer
      s = haer, start = 2, i = 3
>>> hare
   s = hear, start = 1, i = 3
      s = hrae, start = 2, i = 2
>>> hrae
      s = hrae, start = 2, i = 3
>>> hrea
s = hear, start = 0, i = 1
   s = ehar, start = 1, i = 1
      s = ehar, start = 2, i = 2
>>> ehar
      s = ehar, start = 2, i = 3
>>> ehra
   s = ehar, start = 1, i = 2
      s = eahr, start = 2, i = 2
>>> eahr
      s = eahr, start = 2, i = 3
>>> earh
   s = ehar, start = 1, i = 3
      s = erah, start = 2, i = 2
>>> erah
      s = erah, start = 2, i = 3
>>> erha
s = hear, start = 0, i = 2
   s = aehr, start = 1, i = 1
      s = aehr, start = 2, i = 2
>>> aehr
      s = aehr, start = 2, i = 3
>>> aerh
   s = aehr, start = 1, i = 2
      s = aher, start = 2, i = 2
>>> aher
      s = aher, start = 2, i = 3
>>> ahre
   s = aehr, start = 1, i = 3
      s = arhe, start = 2, i = 2
>>> arhe
      s = arhe, start = 2, i = 3
>>> areh
s = hear, start = 0, i = 3
   s = reah, start = 1, i = 1
      s = reah, start = 2, i = 2
>>> reah
      s = reah, start = 2, i = 3
>>> reha
   s = reah, start = 1, i = 2
      s = raeh, start = 2, i = 2
>>> raeh
      s = raeh, start = 2, i = 3
>>> rahe
   s = reah, start = 1, i = 3
      s = rhae, start = 2, i = 2
>>> rhae
      s = rhae, start = 2, i = 3
>>> rhea
*/
