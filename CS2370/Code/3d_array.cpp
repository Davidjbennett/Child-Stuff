#include <iostream>
using namespace std;

int main() {
    int a[][3][4] = {{{1,2,3,4},
                      {5,6,7,8},
                      {9,0,1,2}},
                     {{3,4,5,6},
                      {7,8,9,0},
                      {1,2,3,4}}};

    int n = sizeof(a) / sizeof(a[0]);
    cout << "a has " << n << " top-level elements\n";
    int m = sizeof(a[0]) / sizeof(a[0][0]);
    cout << "Each top-level element of a has " << m << " elements\n";
    int t = sizeof(a[0][0]) / sizeof(a[0][0][0]);
    cout << "Each second-level element of a has " << t << " elements\n";

    for (int i = 0; i < n; ++i) {
        cout << "sizeof(a[" << i << "]): " << sizeof(a[i]) << endl;

        for (int j = 0; j < m; ++j) {
            cout << "sizeof(a[" << i << "][" << j << "]): "
                 << sizeof(a[i][j]) << endl;

            for (int k = 0; k < t; ++k)
                cout << "a[" << i << "][" << j << "][" << k <<"]) = "
                     << a[i][j][k] << endl;
        }
    }
    cout << endl;

    // Using range-based for to print elements
    for (const auto& two_d: a) {
        cout << "2d element:\n";
        for (const auto& one_d: two_d) {
            cout << "\t1d element:\n\t\t";
            for (auto n: one_d)
                cout << n << ' ';
            cout << endl;
        }
        cout << endl;
    }
}

/* Output:
a has 2 top-level elements
Each top-level element of a has 3 elements
Each second-level element of a has 4 elements
sizeof(a[0]): 48
sizeof(a[0][0]): 16
a[0][0][0]) = 1
a[0][0][1]) = 2
a[0][0][2]) = 3
a[0][0][3]) = 4
sizeof(a[0][1]): 16
a[0][1][0]) = 5
a[0][1][1]) = 6
a[0][1][2]) = 7
a[0][1][3]) = 8
sizeof(a[0][2]): 16
a[0][2][0]) = 9
a[0][2][1]) = 0
a[0][2][2]) = 1
a[0][2][3]) = 2
sizeof(a[1]): 48
sizeof(a[1][0]): 16
a[1][0][0]) = 3
a[1][0][1]) = 4
a[1][0][2]) = 5
a[1][0][3]) = 6
sizeof(a[1][1]): 16
a[1][1][0]) = 7
a[1][1][1]) = 8
a[1][1][2]) = 9
a[1][1][3]) = 0
sizeof(a[1][2]): 16
a[1][2][0]) = 1
a[1][2][1]) = 2
a[1][2][2]) = 3
a[1][2][3]) = 4

2d element:
    1d element:
        1 2 3 4 
    1d element:
        5 6 7 8 
    1d element:
        9 0 1 2 

2d element:
    1d element:
        3 4 5 6 
    1d element:
        7 8 9 0 
    1d element:
        1 2 3 4 

*/
