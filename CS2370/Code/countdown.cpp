#include <iostream>
using namespace std;

int main() {
    int n = 5;
    do
        cout << n << "..." << endl;
    while (--n > 0);        // Or n-- > 1
}

/* Output:
5...
4...
3...
2...
1...
*/
