// bin_search.cpp: Binary search
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int bsearch(int a[], int start, int stop, int key) {
    if (stop <= start)
        return -1;

    int mid = (start + stop) / 2;
    if (key < a[mid])
        return bsearch(a, start, mid, key);
    else if (key > a[mid])
        return bsearch(a, mid+1, stop, key);
    else
        return mid;
}

int main() {
    ifstream f("nums.dat");
    int nums[50];

    // Read numbers
    int num, n = 0;
    while (f >> num)
        nums[n++] = num;
    if (!f.eof())
        cout << "File read error\n";
    else {
        cout << "Read " << n << " numbers\n";

        // Sort the array
        sort(nums, nums+n);
        for (int i = 0; i < n; ++i)
            cout << nums[i] << ' ';
        cout << endl;    

        cout << bsearch(nums, 0, n, 3958) << endl;   
    }
}