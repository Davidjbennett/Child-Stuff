// filestream2.cpp: Uses lambda expressions
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ifstream ifs("nums.dat");
    if (ifs) {
        // Read numbers into vector
        vector<int> nums{istream_iterator<int>(ifs), istream_iterator<int>()};

        // Sort them in descending order
        sort(begin(nums), end(nums), [](int num1, int num2){return num1 > num2;});

        // Print only even numbers
        auto even = [](int num) {return num % 2 == 0;};
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
