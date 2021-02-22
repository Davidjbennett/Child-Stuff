// Plain enums (just ints)
#include <iostream>
using namespace std;

int main() {
    enum Color {RED, GREEN, BLUE};  // Type name is optional but recommended
    enum {PENNY=1, NICKEL=5, DIME=10, QUARTER=25};

    cout << RED << endl;
    Color g = GREEN;
    cout << g << endl;
    int b = BLUE;
    cout << b << endl;
    cout << NICKEL+DIME << endl;    // 15 not a valid coin value!
}

/* Output:
0
1
2
15
*/
