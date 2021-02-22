// array_by_ref2.cpp: Uses templates
#include <iostream>
using namespace std;

template<size_t N>
void print_array(int (&a)[N]) {    
    cout << sizeof(a) << endl;
    for (int k: a)
        cout << k << endl;
}

int main() {
    int a[] = {1,2,3,4,5};
    print_array(a);         // 20 == 5*sizeof(int)

    int b[] = {1,2,3};
    print_array(b);
}

/* Output:
20
1
2
3
4
5
12
1
2
3
*/
