#include <iostream>
#include <typeinfo>
using namespace std;

int main() {
    int a[2][3] = {{1,2,3}, {4,5,6}};    // 2 x 3 array with 2 rows
    for (int i = 0; i < 2; ++i)
        cout << sizeof(a[i]) << endl;
    cout << endl;

    for (const auto& row: a)
        cout << sizeof(row) << ' ' << typeid(row).name() << endl;
    cout << endl;

    for (const auto& row: a) {
        for (auto n: row)
            cout << n << ' ';
        cout << endl; 
    }

}

/* Output:
12
12

12
12
*/
