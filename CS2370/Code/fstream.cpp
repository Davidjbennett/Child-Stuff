// fstream.cpp: Shows how to read and write files
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

void read_data(const string& infname, vector<int>& v) {
    ifstream ifs(infname);  // Opens file for input (will close automatically)
    if (!ifs)
        cout << "Could not open " << infname << endl;
    else  {
        int n;
        while (ifs >> n)    // Will break on end-of-file
            v.push_back(n);
    }
}

void write_data(const string& outfname, const vector<int>& v) {
    ofstream ofs(outfname);  // Opens file for output (will close automatically)
    ofs << fixed << setprecision(2);
    for (int n: v)
        ofs << n/100.0 << endl;
}

int main() {
    vector<int> data;
    read_data("nums.dat", data);
    write_data("nums2.dat", data);
}
