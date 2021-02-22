// string-cont.cpp: Shows that strings can be used with generic algorithms
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "What we have here is a Failure to Communicate";

    // Change e's to 3's
    transform(begin(s), end(s), begin(s), [](char c){return c == 'e' ? '3' : c;});
    cout << s << endl;

    // Change everything to lower case
    transform(begin(s), end(s), begin(s), [](char c){return tolower(c);});
    cout << s << endl;
}

/* Output:
What w3 hav3 h3r3 is a Failur3 to Communicat3
what w3 hav3 h3r3 is a failur3 to communicat3
*/
