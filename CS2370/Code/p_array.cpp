#include <iostream>
#include <typeinfo>
using namespace std;

void pass_array(const int stuff[], int n) { // (int* stuff, int n)
    cout << "sizeof(stuff): " << sizeof(stuff) << endl;
    cout << "type of stuff: " << typeid(stuff).name() << endl;
    for (int i = 0; i < n; ++i)
        cout << stuff[i] << ' ';
    cout << endl;
}

int main() {
    int a[] = {1,2,3,4,5};
    cout << "sizeof(a): " << sizeof(a) << endl;
    cout << "type of a: " << typeid(a).name() << endl;
    pass_array(a, 5);
}

/* Output:
p_array.cpp:6:40: warning: sizeof on array function parameter will return size of 'int *' instead of 'int []' [-Wsizeof-array-argument]
    cout << "sizeof(stuff): " << sizeof(stuff) << endl;
                                       ^
p_array.cpp:5:21: note: declared here
void pass_array(int stuff[], int n) {
                    ^
1 warning generated.
sizeof(a): 20
type of a: A5_i
sizeof(stuff): 8
type of stuff: PKi
1 2 3 4 5  
*/
