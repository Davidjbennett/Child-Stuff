// std_list.cpp: Using std::list 
#include <algorithm>
#include <iostream>
#include <iterator> // for ostream_iterator
#include <list>
#include <forward_list>    // for slist
#include <string>
using namespace std;

int main() {
    list<string> words;
    for (const string& word: {"flying", "purple", "people", "eater"})
        words.push_back(word);

    // Can't use std::sort on lists--they are not contiguous in memory
    words.sort();
    for (auto& word: words) 
        cout << word << endl;
    cout << endl;

    // Use a reverse iterator
    for_each(rbegin(words), rend(words), [](const string& s){cout << s << endl;});
    cout << endl;

    // Use slist
    forward_list<string> words2{begin(words), end(words)}; // Copies words
    copy(begin(words2), end(words2), ostream_iterator<string>(cout, "\n"));
}

/* Output:
eater
flying
people
purple

purple
people
flying
eater

eater
flying
people
purple
*/