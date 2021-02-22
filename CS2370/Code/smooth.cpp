#include <iostream>
#include <fstream>
using namespace std;

int smooth_it(int* p) {
    // We assume there are 3 points before and after location p
    int sum = p[-3] + 2*p[-2] + 3*p[-1] + 3*p[0] + 3*p[1] + 2*p[2] + p[3];
    return int(sum/15);
}

int main() {
    const int n = 3072;
    int raw[n], smooth[n];

    // Read in raw data
    ifstream f("2_Record2308.dat");
    int val;
    for (int i = 0; f >> val; ++i)
        raw[i] = val;

    // Copy first 3 and last 3 values to smooth
    for (int i = 0; i < 3; ++i) {
        smooth[i] = raw[i];
        smooth[n-1-i] = raw[n-1-i];
    }

    // Smooth the rest of the values
    for (int i = 3; i < n-3; ++i)
        smooth[i] = smooth_it(raw+i);
}