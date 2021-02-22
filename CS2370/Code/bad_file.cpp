// bad_file.cpp: Catches a bad file name error
#include <fstream>
#include <iostream>
#include <stdexcept>
using namespace std;

void open_file(const string& fname) {
    ifstream ifs(fname);
    if (ifs)
        cout << "File opened successfully\n";
    else
        throw runtime_error("File open error");
}

int main() {
    cout << "Enter file name to open: ";
    string fname;
    cin >> fname;

    try {
        open_file(fname);
    }
    catch (runtime_error& exc) {
        cout << exc.what() << endl;
    }
}

/* Sample run:
$ c++ bad_file.cpp 
$ ./a.out
Enter file name to open: uykuyuj
File open error
*/
