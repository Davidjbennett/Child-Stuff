#include <cstddef>  // For size_t
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Foo {
    string s{"abcdefghijklmnopqrstuvwxyz"};
    vector<int> v{1,2,3,4,5};

public:
    size_t size() const {
        return s.size() + v.size();
    }
};

int main() {
    Foo x;
    cout << sizeof(x) << endl;
    cout << sizeof(string) << endl;
    cout << sizeof(vector<string>) << endl;
    cout << x.size() << endl;
}

/*
56
32
24
31
*/
