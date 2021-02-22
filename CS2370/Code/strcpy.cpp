// Index version (except doesn't return anything. Pointer version is more succinct)
#include <cstring>
#include <iostream>
using namespace std;

void copy(char to[], const char from[]) {
    // We assume that there is enough room in "to"
    int i = -1;
    do {
        ++i;
        to[i] = from[i];
    } while (to[i] != '\0');    // Or while (to[i]);
}

int main() {
    char buffer[81];    // Can hold up to 80 chars
    copy(buffer, "Go ahead, make my day");
    cout << buffer << endl;
    copy(buffer, "Not by a long shot");
    cout << buffer << endl;
}

/* Output:
Go ahead, make my day
Not by a long shot
*/
