// ptr_arith.cpp: Illustrates pointer arithmetic
//
//        Note: The name of an array decays to
//              a pointer to its first element
//              in an expression.
//              (Exception: as argument to sizeof)
//        Also: p[i] == *(p+i) aka &p[i] == p+i
//              (Array indexes use ptr arithmetic!)

#include <iostream>
using namespace std;

int main() {
    int a[] = {1,2,3,4,5};
    cout << sizeof(a) << endl;  // 20

    int* p = a;                 // Same as p = &a[0]
    cout << sizeof(p) << endl;  // 8    No size info!
    cout << "p = " << p << endl;

    cout << *(p+2) << endl;     // 3
    cout << p[2] << endl;       // 3    or: cout << a[2] << endl;
    ++p;                        // p becomes p + sizeof(int)
    cout << "p = " << p << endl;
    cout << p[0] << endl;       // 2    or: cout << *p << endl;
    cout << p[-1] << endl;      // 1    or: cout << *(p-1) << endl;


    // Print backwards
    p = a+4;                    // Point at the 5
    while (p >= a)
        cout << *p-- << ' ';    // Post-decrement operator
    cout << endl; 
}

/* Output:
20
8
p = 0x7ffee649da10
3
3
p = 0x7ffee649da14
2
1
5 4 3 2 1
*/
