// fib1.cpp
#include <cassert>
#include <iostream>
using namespace std;

int fib(int n) {
    assert(n >= 0);
    return (n == 0 || n == 1) ? n : fib(n-1) + fib(n-2);
}

int main() {
    for (int i: {0,1,2,3,4})
        cout << fib(i) << endl;
}

/* Output:
0
1
1
2
3
*/
