#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
using namespace std;

int main() {
    string s1{"the"}, s2{"them"}, s3{"their"};
    multiset<char> m1{begin(s1), end(s1)};
    copy(begin(m1), end(m1), ostream_iterator<char>(cout, " "));
    cout << endl;
    multiset<char> m2{begin(s2), end(s2)};
    multiset<char> m3{begin(s3), end(s3)};
    cout << boolalpha;
    cout << includes(begin(m2), end(m2), begin(m1), end(m1)) << endl;
    cout << includes(begin(m3), end(m3), begin(m1), end(m1)) << endl;
    cout << includes(begin(m3), end(m3), begin(m2), end(m2)) << endl;
}

/* Output:
e h t 
true
true
false
*/
