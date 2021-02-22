#include <iostream>
using namespace std;

void f(int a[], int n) {                        // Identical to void f(int* a, int n) {
    cout << "sizeof(a) " << sizeof(a) << endl;  // a is a pointer

    // Use index notation
    for (int i = 0; i < n; ++i)
        cout << a[i] << ' ';
    cout << '\n';

    // Use pointer arithmetic
    for (int* p = a; p < (a+n); ++p)
        cout << *p << ' ';
    cout << '\n';
}

int main() {
    int stuff[] = {1,2,3,4,5};
    cout << "sizeof(stuff) " << sizeof(stuff) << endl;
    f(stuff, 5);
}

/* Output:
sizeof(stuff) 20
sizeof(a) 8
1 2 3 4 5 
1 2 3 4 5 
*/
