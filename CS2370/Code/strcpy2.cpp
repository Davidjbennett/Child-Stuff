// Pointer implementation of strcpy (except doesn't return anything)
#include <cstring>
#include <iostream>
using namespace std;

void copy(char* to, const char* from) {
    while ((*to++ = *from++) != '\0')
        ;
}

/* Loop above is similar to:
for (; *to != '\0'; ++to, ++from)
    *to = *from;
*/

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