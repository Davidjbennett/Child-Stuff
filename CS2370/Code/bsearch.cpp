#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<int> v{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};
    int key = 44;
    bool ans = binary_search(v.begin(), v.end(), key);
    cout << key << (ans ? " " : " not ") << "found\n";

    // Find the position(s)
    auto [beg, end] = equal_range(v.begin(), v.end(), key);
    int nhits = end - beg;
    cout << nhits << " occurrence(s) of " << key;
    if (nhits > 0) {
        cout << " starting in position " << beg-v.begin() 
             << " and ending in position " << end-v.begin()-1;
    }
    cout << endl;
}

/* Output:
44 found
*/
