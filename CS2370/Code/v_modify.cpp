#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1,2,3,4,5};
    for (int& n: v)        // Note the &
        n += 2;
    for (int n: v)
        cout << n << endl;
}

/* Output:
3
4
5
6
7
*/
