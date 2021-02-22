// filestream.cpp: Reads numbers from a file directly into a vector.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

bool gt(int num1, int num2) {
    return num1 > num2;    // Orders numbers by greater-than (descending order)
}

bool even(int num) {
    return num % 2 == 0;
}

int main() {
    ifstream ifs("nums.dat");
    if (ifs) {
        // Read numbers into vector
        vector<int> nums{istream_iterator<int>(ifs), istream_iterator<int>()};

        // Sort them in descending order
        sort(begin(nums), end(nums), gt);

        // Print only even numbers
        copy_if(begin(nums), end(nums), ostream_iterator<int>(cout, "\n"), even);
    }
}

/* Output:
8948
8716
8292
7370
7194
7004
6934
6148
5982
4800
3958
3220
1804
1748
1660
*/
