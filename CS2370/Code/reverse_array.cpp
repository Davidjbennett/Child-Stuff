#include <algorithm>
#include <iostream>
using namespace std;

void reverse_array(int* array, int n) {
    int* first = array;
    int* last = array + n-1;
    for (int i = 0; i < n/2; ++i)
        iter_swap(first+i, last-i);
}

int main() {
    int a[5] = {1,2,3,4,5};
    reverse_array(a, 5);
    for (int n: a)
        cout << n << ' ';
    cout << endl;
}

/* Output:
5 4 3 2 1
*/
