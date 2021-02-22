// myswap.cpp: Uses references to swap arguments
#include <iostream>
using namespace std;

void myswap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}
int main() {
    int x = 1, y = 2;
    myswap(x,y);
    cout << x << ", " << y << endl;
}
