#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
    ifstream ifs("readlines.cpp");
    string line;
    while (getline(ifs, line))
        cout << line << endl;
}