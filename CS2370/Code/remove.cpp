#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{10, 20, 21, 44, 44, 60, 68, 76, 85, 90};
    auto end_v1 = remove(v1.begin(), v1.end(), 44);
    copy(v1.begin(), end_v1, ostream_iterator<int>(cout, " "));
    cout << endl;

    end_v1 = remove_if(v1.begin(), end_v1, [](int n){return n % 2 == 0;});
    copy(v1.begin(), end_v1, ostream_iterator<int>(cout, " "));
    cout << endl;
}

/* Output:
10 20 21 60 68 76 85 90 
21 85 
*/
