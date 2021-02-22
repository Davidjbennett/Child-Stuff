#include <iostream>
#include <limits>
using namespace std;

int main() {
    auto infinity = numeric_limits<double>::infinity();
    cout << infinity << endl;
    cout << 2.0 / infinity << endl;
}

/* Output:
inf
0
*/
