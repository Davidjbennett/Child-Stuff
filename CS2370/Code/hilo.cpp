// Plays the game of Hi-Lo to illustrate a loop invariant.
// The computer does the guessing.
// The loop ends on lines 16 (if guessed) or 20 (if user cheated).
// .. Note the two ways of terminating the loop.
 
#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Think of a number between 1 and 100" << endl
         << "I will make a guess; "
         << "tell me if I'm (H)igh or (L)ow" << endl;
    int low = 1, high = 100;
    bool guessed = false;

    while(!guessed) {
        // Invariant: the number is in the range [low, high]
        if(low > high) {  // Invariant violation
            cout << "You cheated! I quit" << endl;
            break;  // End loop
        }

        // Try a guess
        int guess = (low + high) / 2;
        cout << "My guess is " << guess << ". ";
        cout << "(H)igh, (L)ow, or (E)qual? ";
        string response;
        cin >> response;

        switch(response[0]) {
        case 'H':
        case 'h':
            high = guess - 1;
            break;
        case 'L':
        case 'l':
            low = guess + 1;
            break;
        case 'E':
        case 'e':
            cout << "I got it!" << endl;
            guessed = true;  // End loop (can't "break" here to end loop)
            break;
        default:
            cout << "Invalid response" << endl;
        }
    }
}
