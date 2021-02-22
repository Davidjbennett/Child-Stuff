#include <iostream>
#include <string>
using namespace std;

template<typename T>
void swap(const T& x, const T& y) {
    T temp = x;
    x = y;
    y = temp;
}

int main() {
    int a = 1, b = 2;
    swap(a, b);
    cout << a << ", " << b << endl; // 2, 1

    string s("one"), t("two");
    swap(s, t);
    cout << s << ", " << t << endl; // two, one
}
