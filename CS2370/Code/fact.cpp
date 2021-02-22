// A factorial function

#include <iostream>
using namespace std;

long long fact(int n) {
    return n <= 1 ? 1 : n*fact(n-1);
}

int main() {
    cout << fact(5) << endl;    // 120
}
