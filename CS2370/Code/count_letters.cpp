#include <cctype>
#include <iostream>
#include <string>
using namespace std;

int main() {
   string input_word;
   cout << "Enter a word: ";
   cin  >> input_word;

   int num_letters = 0;
   for (char c: input_word) {
      if (isalpha(c)) {
         num_letters += 1;
      }
   }

   cout << "Number of letters: " << num_letters << endl;
}

/* Sample execution:
Enter a word: daff0d1l 
Number of letters: 6
*/
