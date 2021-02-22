#include <iostream>
using namespace std;

int main() {
    int a[][3][4] = {{{1,2,3,4},{5,6,7,8},{9,0,1,2}},
                     {{3,4,5,6},{7,8,9,0},{1,2,3,4}}};

    cout << "sizeof(a): " << sizeof(a) << endl;

    size_t n = sizeof(a) / sizeof(a[0]);
    for (size_t i = 0; i < n; ++i) {
        cout << "sizeof(a[" << i << "]): " << sizeof(a[i]) 
             << endl;

        size_t m = sizeof(a[i]) / sizeof(a[i][0]);
        for (size_t j = 0; j < m; ++j) {
            cout << "sizeof(a[" << i << "][" << j << "]): "
                 << sizeof(a[i][j]) << endl;

            size_t t = sizeof(a[i][j]) / sizeof(a[i][j][0]);
            for (size_t k = 0; k < t; ++k)
                cout << "a[" << i << "][" << j << "][" << k 
                     << "] == " << a[i][j][k] << endl;
        }
    }
}

/* Output:
sizeof(a): 96
sizeof(a[0]): 48
sizeof(a[0][0]): 16
a[0][0][0] == 1
a[0][0][1] == 2
a[0][0][2] == 3
a[0][0][3] == 4
sizeof(a[0][1]): 16
a[0][1][0] == 5
a[0][1][1] == 6
a[0][1][2] == 7
a[0][1][3] == 8
sizeof(a[0][2]): 16
a[0][2][0] == 9
a[0][2][1] == 0
a[0][2][2] == 1
a[0][2][3] == 2
sizeof(a[1]): 48
sizeof(a[1][0]): 16
a[1][0][0] == 3
a[1][0][1] == 4
a[1][0][2] == 5
a[1][0][3] == 6
sizeof(a[1][1]): 16
a[1][1][0] == 7
a[1][1][1] == 8
a[1][1][2] == 9
a[1][1][3] == 0
sizeof(a[1][2]): 16
a[1][2][0] == 1
a[1][2][1] == 2
a[1][2][2] == 3
a[1][2][3] == 4
*/
