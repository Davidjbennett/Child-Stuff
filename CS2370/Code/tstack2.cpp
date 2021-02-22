// tstack2.cpp: Separate compilation from stack2.cpp
#include "stack2.h"
#include <iostream>
using namespace std;
// No need to include <vector>; that's Stack's secret.

// No change to main
int main() {    
    Stack s1;   // Uses default constructor
    for (int i = 0; i < 5; ++i)
        s1.push(i);
    cout << "s1.size() = " << s1.size() << ", top = " << s1.top() << endl;

    // Copy s1 to s2 (uses synthesized copy constructor) 
    Stack s2(s1);   
    cout << "s2.size() = " << s2.size() << ", top = " << s2.top() << endl;

    // Add elements to s2
    for (int i = 5; i < 10; ++i)
        s2.push(i);
    cout << "s2.size() = " << s2.size() << ", top = " << s2.top() << endl;

    // Pop some elements from s2
    cout << "popping " << s2.pop() << " from s2\n";
    cout << "popping " << s2.pop() << " from s2\n";

    // Assign s2 to s1 (uses synthesized assignment operator)
    s1 = s2;

    // Empty s1
    while (s1.size() > 0)
        cout << s1.pop() << ' ';
    cout << endl;
    cout << "s1.size() = " << s1.size() << endl;
    cout << "s2.size() = " << s2.size() << endl;
}

/* Output:
s1.size() = 5, top = 4
s2.size() = 5, top = 4
s2.size() = 10, top = 9
popping 9 from s2
popping 8 from s2
7 6 5 4 3 2 1 0 
s1.size() = 0
s2.size() = 8
*/
