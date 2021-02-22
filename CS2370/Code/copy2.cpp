// copy2.cpp: Illustrates back_inserter (although it's not needed here)
//            and vector constructor that takes iterators from any sequence.
//            
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};
    vector<int> v2;

    // Only copy even numbers
    copy_if(v1.begin(), v1.end(), back_inserter(v2), [](int n){return n % 2 == 0;});
    for (int x: v2)
        cout << x << ' ';
    cout << endl;

    // An even better way to *initialize* a *new* sequence from another
    vector<int> v3(v1.begin(), v1.end());   // No need for back_inserter
    copy(v3.begin(), v3.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
}

/* Output:
10 20 44 44 60 68 76 90 
10 20 21 44 44 60 68 76 85 90 
*/
