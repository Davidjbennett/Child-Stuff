#include <iostream>
#include <string>
using namespace std;

int

char PrintMenu(string Uin){
   char User_Char;

      cout << "MENU" << endl;
      cout << "c - " << "Number of non-whitespace characters" << endl;
      cout << "w - " << "Number of words" << endl;
      cout << "f - " << "Find text" << endl;
      cout << "r - " << "Replace all !'s" << endl;
      cout << "s - " << "Shorten spaces" << endl;
      cout << "q - " << "Quit\n" << endl;
      cout << "Choose an option: " << endl;

      cin >> User_Char;

      switch (User_Char){
      case 'c':
         int Non_White_Chars;
         Non_White_Chars = 0;
         for(int i = 0; i < Uin.length(); i++){
            if(!isspace(Uin[i])){
               Non_White_Chars++;
            }
         }
         cout << "Number of non-whitespace characters: " << Non_White_Chars << endl << endl;
         break;
      case 'w':
         int Num_Of_Words;
         Num_Of_Words = 1;
         for(int i = 0; i <= Uin.length(); i++){
            if(isspace(Uin[i])){
               Num_Of_Words++;
            }
         }
         cout << "Number of words: " << Num_Of_Words << endl << endl;
         break;
      case 'f':
         break;
      case 'r':
         break;
      case 's':
         break;
      case 'q':
         return User_Char;
         break;
      
      default:
         cout << "Invalid Choice." << endl;
         break;
      }
   
   
}

int main() {

   cout << "Enter a sample text:" << endl;
   string tempS;
   string Userin;

   getline(cin, tempS);
   Userin.append(tempS);

   // while (getline(cin, tempS)){
   //    Userin.append(tempS);
   //    Userin.append("\n");
   // }

   cout << "You entered: " << Userin << endl;
   
   PrintMenu(Userin);

   return 0;
}