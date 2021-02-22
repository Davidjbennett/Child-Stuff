// sstate.cpp: Illustrates stream state
#include <iostream>
#include <string>
using namespace std;

void str_state(istream& is) {
    if (is.good())
        cout << "good ";
    if (is.eof())
        cout << "eof " ;
    if (is.fail())
        cout << "fail ";
    cout << endl;
}

int main() {
    for (;;) {  // "Infinite" loop (breaks on "end-of-file" entry)
        int n;
        cout << "Enter a number (or signal eof to quit): ";
        cin >> n;
        str_state(cin);

        if (cin)                // Same as cin.good()
            cout << "you entered " << n << endl;
        else if (cin.eof())     // This check must precede fail check!
            break;
        else if (cin.fail()) {
            // Bad input
            string s;
            cin.clear();        // Re-enable input
            getline(cin, s);    // Extract bad input   
            cout << "input error\n";
        }
    }
}

/* Sample execution:
$ ./a.out
Enter a number (or signal eof to quit): 2
good 
you entered 2
Enter a number (or signal eof to quit): two
fail 
input error
Enter a number (or signal eof to quit): ^Deof fail 
*/
