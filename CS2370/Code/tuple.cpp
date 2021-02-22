// tuple.cpp: Illustrates pair and tuples
#include <iostream>
#include <string>
#include <tuple>
#include <utility>  // For pair
#include <vector>
using namespace std;

int main() {
    // A vector of pairs (universal initialization syntax)
    vector<pair<int,string>> v{{1,"one"s}, {2,"two"s}};
    cout << v[0].first << ", " << v[0].second << endl;
    cout << endl;

    // Use structured bindings to extract items from pair
    for (auto& [k,v]: v)
        cout << k << ", " << v << endl;
    cout << endl;

    // Illustrate tuples
    using triple = tuple<int, double, string>;
    triple t(1, 2.5, "three");
    auto x = get<0>(t);
    auto [_, y, z] = t;
    cout << x << ", " << y << ", " << z << '\n';    // 1, 2.5, three
}

/* Output:
1, one

1, one
2, two

1, 2.5, three
*/
