#include <iostream>
#include <vector>
using namespace std;

using namespace std;

string s;
string menuSelect;

vector<int> jerseyNum;
vector<int> playerRating;


void outputRoster(){
   for (int i = 0; i < jerseyNum.size(); i++)
    {
       cout << "Player " << (i + 1) << "-- Jersey number: " 
       << jerseyNum.at(i) << ", Rating: " << playerRating.at(i) << endl;
    } 
}


int main() {
    int count = 0;

    while (count < 5){
       cout << "Enter player " << (count+1) << "\'s jersey number:" << endl;
       getline(cin,s);
       jerseyNum.push_back(stoi(s));
       cout << "Enter player " << count << "\'s rating:" << endl;
       getline(cin, s);
       playerRating.push_back(stoi(s));
       s = "";
       count++;
    }

    cout << "ROSTER" << endl;
    outputRoster(jerseyNum,playerRating);

    cout << "a - Add player\n";
    cout << "d - Remove player\n";
    cout << "u - Update player rating\n";
    cout << "r - Output players above a rating\n";
    cout << "o - Output roster\n";
    cout << "q - Quit\n\n";
    cout << "Choose an option:\n";
    getline(cin, menuSelect);

    do{
        switch (menuSelect){
            case 'a':
                cout << "Enter a new player's jersey number:\n";
                cin >> jerseyNumber;
                while (jerseyNumber < 0 || jerseyNumber > 99) {
                    cout << "Enter a new player's jersey number (0 - 99):\n";
                    cin >> jerseyNumber;
                }
                cout << "Enter player\'s rating:" << endl;
                getline(cin, s);
                playerRating.push_back(stoi(s));
                s = "";
                break;
            case 'd':
                break;
            case 'u':
                break;
            case 'r':
                break;
            case 'o': outputRoster();
                break;
            case 'q':
                break;
            default:
                break;
        }
    } while (menuSelect != 'q');
    
    return 0;
}