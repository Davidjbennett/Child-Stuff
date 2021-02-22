#include <iostream>
using namespace std;

int main() {
    double x = 9007199254740993.0;
    cout.precision(20);
    cout << x << endl;      // 9007199254740992
    cout << x+1.0 << endl;  // 9007199254740992
    cout << x+2.0 << endl;  // 9007199254740994
}