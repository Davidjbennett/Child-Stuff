#include <iostream>
using namespace std;

int main() {
    int a[][2][3][4] = {{{{1,2,3,4},     // Start of a[0]
                          {5,6,7,8},
                          {9,0,1,2}},
                         {{3,4,5,6},
                          {7,8,9,0},
                          {1,2,3,4}}},
                        {{{5,6,7,8},     // Start of a[1]
                          {9,0,1,2},
                          {3,4,5,6}},
                         {{7,8,9,0},
                          {1,2,3,4},
                          {5,6,7,8}}}};

    // Using range-based for to print elements
    for (const auto& three_d: a) {
        cout << "3d element (" << sizeof(three_d) << " bytes):\n";
        for (const auto& two_d: three_d) {
            cout << "\t2d element (" << sizeof(two_d) << " bytes):\n";
            for (const auto& one_d: two_d) {
                cout << "\t\t1d element (" << sizeof(one_d) << " bytes):\n\t\t\t";
                for (auto n: one_d)
                    cout << n << ' ';
                cout << endl;
            }
            cout << endl;
        }
    }
}

/* Output:
3d element (96 bytes):
    2d element (48 bytes):
        1d element (16 bytes):
            1 2 3 4 
        1d element (16 bytes):
            5 6 7 8 
        1d element (16 bytes):
            9 0 1 2 

    2d element (48 bytes):
        1d element (16 bytes):
            3 4 5 6 
        1d element (16 bytes):
            7 8 9 0 
        1d element (16 bytes):
            1 2 3 4 

3d element (96 bytes):
    2d element (48 bytes):
        1d element (16 bytes):
            5 6 7 8 
        1d element (16 bytes):
            9 0 1 2 
        1d element (16 bytes):
            3 4 5 6 

    2d element (48 bytes):
        1d element (16 bytes):
            7 8 9 0 
        1d element (16 bytes):
            1 2 3 4 
        1d element (16 bytes):
            5 6 7 8 
*/
