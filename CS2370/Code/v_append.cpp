#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;
    ifstream f("nums.dat");     // Open text file
    int num;                    // Variable for input

    // Read and append numbers
    while (f >> num)
        v.push_back(num);

    // Print them
    cout << "Size: " << v.size() << endl;
    for (int n: v)
        cout << n << ' ';
    cout << endl;
}

/* Output:
Size: 21
5737 8716 5982 1804 6148 7004 5861 8292 3958 8948 3307 7194 1748 4800 1660 4131 8275 7370 9081 6934 3220 
*/
