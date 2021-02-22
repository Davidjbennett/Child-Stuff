#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number between 1 and 5: ";
    cin >> n;
    while (n < 1 || n > 5) {
        cout << "Enter a number between 1 and 5: ";
        cin >> n;
    }
    cout << "You entered: " << n << endl;
}