#include <bitset>
#include <iostream>
using namespace std;

int main() {
    cout << "Enter an integer to extract from: ";
    unsigned int n;
    cin >> n;
    cout << "n = " << n << " = " << bitset<32>(n) << endl;

    cout << "Enter the number of lower bits: ";
    unsigned int k;
    cin >> k;

    unsigned int mask = (1 << k) - 1;
    auto result = n & mask;
    cout << "lower " << k << " bits unchanged: " << bitset<32>(result) << endl;
}

/*  Sample execution:
Enter an integer to extract from: 60000
n = 60000 = 00000000000000001110101001100000
Enter the number of lower bits: 10
lower 10 bits unchanged: 00000000000000000000001001100000
*/
