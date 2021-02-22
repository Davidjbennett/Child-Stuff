#include <iomanip>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};

    // Add 1 to each element in place
    transform(v1.begin(), v1.end(), v1.begin(), [](int n){return n+1;});
    copy(v1.begin(), v1.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    // Place the residue mod 5 of each element from v1 into v2
    vector<int> v2(v1.size());
    transform(v1.begin(), v1.end(), v2.begin(), [](int n){return n%5;});
    copy(v2.begin(), v2.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    // Place v1*v3 in v4
    vector<float> v3{22.0, 87.7, 11.2, 12.2, 27.1, 98.9, 22.1, 96.0, 58.6, 26.0};
    vector<float> v4(v1.size());
    transform(v1.begin(), v1.end(), v3.begin(), v4.begin(), [](int n, float x){return n*x;});
    cout << setprecision(2) << fixed;
    copy(v4.begin(), v4.end(), ostream_iterator<float>(cout, " "));
    cout << endl;    
}

/* Output:
11 21 22 45 45 61 69 77 86 91 
1 1 2 0 0 1 4 2 1 1 
242.00 1841.70 246.40 549.00 1219.50 6032.90 1524.90 7392.00 5039.60 2366.00 
*/
