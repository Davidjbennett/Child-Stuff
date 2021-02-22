#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct gt_n {
    int key;
    gt_n(int key) {
        this->key = key;
    }
    bool operator()(int n) {
        return n > key;
    }
};

int  main() {
   vector<int> v = {15,6,25,18,9,23,20,7,18,1};
   auto iter = v.begin();
   while ((iter = find_if(iter, v.end(), gt_n(15))) != v.end())
       cout << *iter++ << ' ';
   cout << endl;
}
/* Output:
25 18 23 20 18 
*/
