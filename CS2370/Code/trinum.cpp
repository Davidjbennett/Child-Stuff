// trinum.cpp: Recursively computes the nth triangular number
#include <iostream>
using namespace std;

int trinum(int n) {
    return (n <= 1) ? 1 : trinum(n-1) + n;
}

int main() {
    for (int n: {1,2,3,4})
        cout << trinum(n) << endl;
}