#include <cstddef>
#include <iostream>
using namespace std;

template<size_t N, size_t M>
void print_array(int (&a)[N][M]) {
    for (auto& row: a)
        for (int elem: row)
            cout << elem << endl;
}

int main() {
    int a[2][3] = {{1,2,3}, {4,5,6}};
    int b[3][2] = {{6,5}, {4,3}, {2,1}};
    print_array(a);
    print_array(b);
}