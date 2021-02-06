#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Vectors
    vector<int> jerseys;
    vector<int> ratings;
    vector<int> playerNum = {1,2,3,4,5,6,7,8,9};

    int jerseyNumber, rating;
    char option;

    for (int i = 0; i < 5; i++) {
        cout << "Enter player " << i + 1 << "'s jersey number:\n";
        cin >> jerseyNumber;
        while (jerseyNumber < 0 || jerseyNumber > 99) {
            cout << "Enter player " << i + 1 << "'s jersey number (0 - 99):\n";
            cin >> jerseyNumber;
        }
        jerseys.push_back(jerseyNumber);

        cout << "Enter player " << i + 1 << "'s rating:" << endl;
        cin >> rating;
        while (rating < 1 || rating > 9) {
            cout << "Enter player " << i + 1 << "'s rating (1 - 9):\n";
            cin >> rating;
        }
        ratings.push_back(rating);
        cout << "\n";
    }

    cout << "ROSTER\n";
    for (int i = 0; i < jerseys.size(); i++) {
        cout << "Player " << i + 1 << " -- Jersey number: " << jerseys[i] << ", Rating: " << ratings[i] << "\n";
    }
    cout << "\n";

    do {
        cout << "MENU\n";
        cout << "a - Add player\n";
        cout << "d - Remove player\n";
        cout << "u - Update player rating\n";
        cout << "r - Output players above a rating\n";
        cout << "o - Output roster\n";
        cout << "q - Quit\n\n";

        cout << "Choose an option:";
        cin >> option;

        switch (option) {
            case 'o':
                cout << "\nROSTER\n";
                for (int i = 0; i < jerseys.size(); i++) {
                    cout << "Player " << i + 1 << " -- Jersey number: " << jerseys[i] << ", Rating: " << ratings[i] << "\n";
                }
                break;

            case 'a':
                cout << "Enter a new player's jersey number:\n";
                cin >> jerseyNumber;
                while (jerseyNumber < 0 || jerseyNumber > 99) {
                    cout << "Enter a new player's jersey number (0 - 99):\n";
                    cin >> jerseyNumber;
                }
                jerseys.push_back(jerseyNumber);

                cout << "Enter the player's rating:" << endl;
                cin >> rating;
                while (rating < 1 || rating > 9) {
                    cout << "Enter the player's rating (1 - 9):\n";
                    cin >> rating;
                }
                ratings.push_back(rating);
                break;

            case 'd':
                cout << "Enter a jersey number:\n";
                cin >> jerseyNumber;
                for (int i = 0; i < jerseys.size(); i++) {
                    if (jerseys[i] == jerseyNumber) {
                        jerseys.erase(jerseys.begin() + i);
                        ratings.erase(ratings.begin() + i);
                        break;
                    }
                }
                break;

            case 'u':
                cout << "Enter a jersey number:\n";
                cin >> jerseyNumber;
                cout << "Enter a new rating for player:\n";
                cin >> rating;
                while (rating < 1 || rating > 9) {
                    cout << "Enter a new rating for player (1 - 9):\n";
                    cin >> rating;
                }

                for (int i = 0; i < jerseys.size(); i++) {
                    if (jerseys[i] == jerseyNumber) {
                        ratings[i] = rating;
                    }
                }
                break;

            case 'r':
                cout << "Enter a rating:\n";
                cin >> rating;
                cout << "ABOVE " << rating << "\n";
                for (int i = 0, count = 0; i < ratings.size(); i++) {
                    if (ratings[i] > rating) {
                        count++;
                        cout << "Player " << playerNum.at(i) << " -- Jersey number: " << jerseys[i] << ", Rating: " << ratings[i] << "\n";
                    }
                }
                break;

            case 'q':
                break;

            default:
                cout << "Invalid option. Try again.\n";
        }
        cout << "\n";
    } while (option != 'q');

    return 0;
}