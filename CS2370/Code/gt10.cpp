#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool gt10(int n) {
   return n > 10;
}

int  main() {
   vector v<int> = {15,6,25,18,9,23,20,7,18,1};
   auto iter = v.begin();
   while ((iter = find_if(iter, v.end(), gt10)) != v.end())
       cout << *iter++ << ' ';
   cout << endl;
}
