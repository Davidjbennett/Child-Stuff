#include <iostream>
using namespace std;

int main() {
    int a[][3] = {{1,2,3},{4,5,6},{7,8,9}};

    cout << "sizeof(a): " << sizeof(a) << endl;
    size_t n = sizeof(a) / sizeof(a[0]);

    for (size_t i = 0; i < n; ++i) {
        cout << "sizeof(a[" << i << "]): " << sizeof(a[i]) 
             << endl;

        size_t m = sizeof(a[i]) / sizeof(int);
        for (size_t j = 0; j < m; ++j)
            cout << "a[" << i << "][" << j << "] == " 
                 << a[i][j] << endl;
    }
}

/* Output:
sizeof(a): 36
sizeof(a[0]): 12
a[0][0] == 1
a[0][1] == 2
a[0][2] == 3
sizeof(a[1]): 12
a[1][0] == 4
a[1][1] == 5
a[1][2] == 6
sizeof(a[2]): 12
a[2][0] == 7
a[2][1] == 8
a[2][2] == 9
*/
