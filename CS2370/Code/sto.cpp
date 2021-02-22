#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "123", t = "4.5";
    int n = stoi(s);
    double x = stod(t);
    cout << n << " + " << x << " = " << n+x << endl;
}

/* Output:
123 + 4.5 = 127.5
*/
