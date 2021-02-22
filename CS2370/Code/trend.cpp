// trend.cpp: Computes a moving average of a list of numbers.
//            Uses a window of size 3 (Note: window size should be odd)

#include <iomanip>
#include <iostream>
using namespace std;

void trend(float* result, float* numbers, int size) {   // float* == float[]  
    // First and last elements are unchanged
    result[0] = numbers[0];
    result[size-1] = numbers[size-1];

    // Start at second element, end at next-to-last
    for (int i = 1; i < size-1; ++i)
        result[i] = (numbers[i-1] + numbers[i] + numbers[i+1]) / 3.0;
}

int main() {
    float nums[] = 
        {174.0, 174.2, 174.1, 174.7, 174.2, 175.2, 176.2, 175.6, 176.2, 174.8, 
         174.4, 174.9, 175.7, 175.5, 175.7, 174.2, 173.8, 175.0, 173.9, 173.7};
    const int SIZE = sizeof(nums) / sizeof(float);
    float avg[SIZE];

    trend(avg, nums, SIZE);

    cout << fixed << setprecision(1);
    for (float val: avg)
        cout << val << ' ';
    cout << endl;
}

/* Output:
174.0 174.1 174.3 174.3 174.7 175.2 175.7 176.0 175.5 175.1 174.7 175.0 175.4 175.6 175.1 174.6 174.3 174.2 174.2 173.7 
*/
