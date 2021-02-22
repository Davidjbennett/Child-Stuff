#include <algorithm>
#include <cstddef>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<int> v1{1,2,3,4,5};
    vector<string> v2{"a", "pig", "in", "a", "poke"};

    // Find sums
    cout << accumulate(v1.begin(), v1.end(), 0) << endl;
    cout << accumulate(v2.begin(), v2.end(), ""s) << endl;

    // Find product
    cout << accumulate(v1.begin(), v1.end(), 1, [](int acc, int x){return acc*x;}) << endl;

    // Find max
    auto small = numeric_limits<int>::min();
    cout << accumulate(v1.begin(), v1.end(), small, [](int acc, int x){return max(acc,x);}) << endl;
    cout << accumulate(v2.begin(), v2.end(), ""s, [](const string& acc, const string& x){return max(acc,x);}) << endl;

    // Find max string length
    auto biglen = [](size_t acc, const string& x) {return max(acc, x.size());};
    cout << accumulate(v2.begin(), v2.end(), 0, biglen) << endl;
}

/* Output:
15
apiginapoke
120
5
poke
poke
4
*/
