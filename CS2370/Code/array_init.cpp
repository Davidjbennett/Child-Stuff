#include <iostream>
using namespace std;

int main() {
    int a[3];               // Uninitalized
    for (auto i: a)
        cout << i << endl;
    cout << endl;

    int b[3] = {};          // Zero-initialized
    for (auto i: b)
        cout << i << endl;

    int c[] = {1,2,3};      // Explicitly initialized (and sized)
    for (auto i: c)
        cout << i << endl;
}

/* Output:
0
-473261392
32766

0
0
0
*/
