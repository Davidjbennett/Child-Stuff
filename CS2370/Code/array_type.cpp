#include <iostream>
#include <typeinfo>
using namespace std;

void arr_type(int a[]) {   // Same as `int* a`. Size is lost
    cout << typeid(a).name() << endl;
}

int main() {
    int a[3];
    cout << typeid(a).name() << endl;
    int b[4];
    cout << typeid(b).name() << endl;
    cout << boolalpha << (typeid(a) == typeid(b)) << endl;
    arr_type(a);
    arr_type(b);
}

/* Output:
A3_i
A4_i
false
Pi
Pi
*/
