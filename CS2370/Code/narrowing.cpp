#include <iostream>
using namespace std;

int main() {
    int n = 3 / 2;
    auto m = 3 / 2.0;
    int k{3 / 2.0};
    cout << n << ", " << m << ", " << k << endl;
}

/* Output:
1, 1.5, 1
*/
