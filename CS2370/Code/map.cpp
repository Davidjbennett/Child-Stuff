// map.cpp: Builds a word length count map. Uses pairs explicitly.

// Note: at() returns a reference. find returns an iterator.

#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    // Read file of words and track by word length
    map<int, int> wlength;
    string word;
    ifstream ifs("words.txt");
    while (ifs >> word) {
        auto len = word.size();
        if (wlength.find(len) != wlength.end())
            ++wlength.at(len);
        else
            wlength.emplace(len, 1);
    }

    for (const auto& pair: wlength)
        cout << pair.first << ": " << pair.second << endl;
}

/* Output:
2: 62
3: 643
4: 2542
5: 5116
6: 8297
7: 11569
8: 12678
9: 11761
10: 9890
11: 7358
12: 5065
13: 3036
14: 1690
15: 945
16: 450
17: 233
18: 83
19: 43
20: 9
21: 9
22: 3
23: 1
24: 1
*/
