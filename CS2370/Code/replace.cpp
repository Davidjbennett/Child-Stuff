#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};

    // Replace 44 with 45
    replace(v1.begin(), v1.end(), 44, 45);
    for (auto x: v1)
        cout << x << ' ';
    cout << endl;

    // Replace even numbers with -1
    replace_if(v1.begin(), v1.end(), [](int n){return n % 2 == 0;}, -1);
    for (auto x: v1)
        cout << x << ' ';
    cout << endl;
}

/* Output:
10 20 21 45 45 60 68 76 85 90 
-1 -1 21 45 45 -1 -1 -1 85 -1 
*/
