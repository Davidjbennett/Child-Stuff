// count_static.cpp: Illustrates a local static
#include <iostream>
using namespace std;

int count() {
    static int n = 0;   // Local scope!
    return ++n;
}

int main() {
    for (int i = 0; i < 5; ++i)
        cout << count() << endl;
}