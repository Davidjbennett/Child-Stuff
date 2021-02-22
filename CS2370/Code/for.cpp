#include <iostream>
using namespace std;

int main () {
    int i = 0;
    while (i < 5) {
        cout << i << ' ';
        ++i;
    }
    cout << endl;

    for (int i = 0; i < 5; ++i)
        cout << i << ' ';
    cout << endl;
}

/* Output:
0 1 2 3 4 
0 1 2 3 4 
*/