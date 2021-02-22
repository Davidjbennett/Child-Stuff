#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter an integer: ";
    cin >> num;
    bool is_prime = true;

    // Check for even first
    if (num > 2 && num % 2 == 0)
        is_prime = false;
    else {
        // Check odd numbers up through sqrt(num)
        for (int factor = 3; factor <= sqrt(num); factor += 2)
            if (num % factor == 0) {
                is_prime = false;
                break;
            }
    }
    cout << num << " is " << (is_prime ? "" : "not ") << "prime\n";
}