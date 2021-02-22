// fib2.cpp: An iterative fibonacci solution (uses tuple assignment)
#include <cassert>
#include <iostream>
#include <tuple>
using namespace std;

int fib(int n) {
    assert(n >= 0);
    if (n == 0 || n == 1)   // Base cases
        return n;

    int curr = 0;
    int next = 1;
    for (int i = 2; i <= n; ++i)
        tie(curr, next) = make_tuple(next, curr+next);
    return next;
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
