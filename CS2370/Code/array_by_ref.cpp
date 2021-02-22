// array_by_ref.cpp
#include <iostream>
using namespace std;

void print_array(int (&a)[5]) {    
    cout << sizeof(a) << endl;
    for (int k: a)
        cout << k << endl;
}

int main() {
    int a[] = {1,2,3,4,5};
    print_array(a);         // 20 == 5*sizeof(int)

/*
    int b[] = {1,2,3};
    print_array(b);

    b is of the wrong size. Here is the error message:

    "candidate function not viable: no known conversion from 'int [3]' to 'int (&)[5]' for 1st argument
void print_array(int (&a)[5]) {"
*/   

}

/* Output:
20
1
2
3
4
5
*/
