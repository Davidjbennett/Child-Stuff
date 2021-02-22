#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1,2,3,4,5};
    v.resize(10);
    for (auto n: v)
        cout << n << endl;
}
