#include <iostream>
using namespace std;

void hanoi(const string& start, const string& target,
           const string& other, int ndiscs) {
    if (ndiscs == 1)
        cout << "move from " << start << " to " << target << endl;
    else {
        hanoi(start, other, target, ndiscs-1);
        hanoi(start, target, other, 1);
        hanoi(other, target, start, ndiscs-1);
    }
}

int main() {
    hanoi("peg-1", "peg-2", "peg-3",1);
    cout << endl;    
    hanoi("peg-1", "peg-2", "peg-3",2);
    cout << endl;    
    hanoi("peg-1", "peg-2", "peg-3",3);
    cout << endl;    
}

/* Output:
move from peg-1 to peg-2

move from peg-1 to peg-3
move from peg-1 to peg-2
move from peg-3 to peg-2

move from peg-1 to peg-2
move from peg-1 to peg-3
move from peg-2 to peg-3
move from peg-1 to peg-2
move from peg-3 to peg-1
move from peg-3 to peg-2
move from peg-1 to peg-2
*/
