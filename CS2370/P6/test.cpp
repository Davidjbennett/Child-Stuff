#include <cstdlib>
#include <set>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;
vector<string> words;

int main(){
    string a = "apples";

    // string a2 = a.substr(1,5) + a.substr(0,1);

    for(int i = 0; i < a.length(); i++){
        string s = a.substr(i,a.length()) + a.substr(0,i);
        cout << s << endl;
    }
}