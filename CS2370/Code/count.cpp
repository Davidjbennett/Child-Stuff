#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<string> v{"a", "pig", "in", "a", "poke"};
    cout << count(v.begin(), v.end(), "a") << endl;
    cout << count(v.begin(), v.end(), "the") << endl;
    cout << count_if(v.begin(), v.end(), [](const string& s){return s.size() > 2;}) << endl;
}

/* Output:
2
0
2
*/