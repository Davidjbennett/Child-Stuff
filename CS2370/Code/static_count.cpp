// static_count.cpp: Illustrates a "local" static variable
#include <iostream>
using namespace std;

int count() {
    static int n = 0;
    return ++n;
}

int main() {
    for (int i = 0; i < 5; ++i)
        cout << count() << endl;
}

/* Output:
1
2
3
4
5
*/
