#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};
    vector<int> v2;
    v2.resize(v1.size());
    copy(v1.begin(), v1.end(), v2.begin());
    for (int x: v2)
        cout << x << ' ';
    cout << endl;

    vector<int> v3(v1);
    assert(equal(v1.begin(), v1.end(), v3.begin()) && v1.size() == v3.size());

    // Only copy even numbers
    auto end_v2 = copy_if(v1.begin(), v1.end(), v2.begin(), [](int n){return n % 2 == 0;});
    v2.resize(end_v2 - v2.begin());   // Truncate v2
    for (int x: v2)
        cout << x << ' ';
    cout << endl;

}

/* Output:
10 20 21 44 44 60 68 76 85 90 
10 20 44 44 60 68 76 90 
*/
