// list1.cpp: Using std::list (inserts elements in alpha order)
#include <iostream>
#include <list>
#include <string>
using namespace std;

void insert(list<string>& alist, const string& s) {
    // Find pointer before which the new node should go
    auto p = alist.begin();
    while (p != alist.end() && s > *p)
        ++p;
    alist.insert(p, s);
}

int main() {
    list<string> words;
    for (const string& word: {"flying", "purple", "people", "eater"})
        insert(words, word);

    for (const string& s: words)
        cout << s << ' ';
    cout << endl;
}

/* Output:
eater flying people purple 
*/
