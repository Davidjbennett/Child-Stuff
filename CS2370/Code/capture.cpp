// capture.cpp: Illustrates lambda capture

#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
    // Read in nums.dat
    ifstream ifs("nums.dat");
    if (ifs) {
        // Read numbers into vector
        vector<int> nums{istream_iterator<int>(ifs), istream_iterator<int>()};

        // Example 1: Capture an input integer
        cout << "Enter a comparison number in the range [1000,9999]: ";
        int num;
        cin >> num;
        if (cin) {
            copy_if(begin(nums), end(nums), ostream_iterator<int>(cout, "\n"),
                [num](int n){return n < num;});
        }
        cout << endl;

	int lastnum = 0;
        // Example 2: Make everything odd, but capture the last number
        auto make_odd = [&lastnum](int n){lastnum = n; return n%2 == 0 ? n+1 : n;};
        transform(begin(nums), end(nums), begin(nums), make_odd);
        copy(begin(nums), end(nums), ostream_iterator<int>(cout, "\n"));

	cout << lastnum << endl;
    }
}

/* Sample execution:
Enter a comparison number in the range [1000,9999]: 4000
1804
3958
3307
1748
1660
3220

5737
8717
5983
1805
6149
7005
5861
8293
3959
8949
3307
7195
1749
4801
1661
4131
8275
7371
9081
6935
3221
*/
