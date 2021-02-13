#include <iostream>
#include <string>
using namespace std;

/* Outputs the sting without whitespace */
string OutputWithoutWhitespace(string usrStr) {
  
  string newString; 
  int index;
  
  while(true) {
    
   index = usrStr.find(" ");
   if (index == -1) {
     break;
   }
   
   newString = usrStr.substr(0, index);
   usrStr.replace(0, index + 1, newString);
  }
  
  return usrStr;
}

/* (3)Implement the GetNumOfNonWSCharacters that returns the number of non-whitespace characters */
int GetNumOfNonWSCharacters(string words) {
  
  int numOfNonWSChars;
  
  numOfNonWSChars = OutputWithoutWhitespace(words).size();
  
  return numOfNonWSChars;
  
}


/*(4)Implement GetNumOfWords function that returns the number of words in the string */
int GetNumOfWords(const string usrStr) {
  string String = usrStr;
  string newString; 
  int index;
  int numWords = 1;
  
  if (String.size() == 0) {
    return 0;   
  }
  while(true) {
    
   index = String.find(" ");
   if (index == -1) {
     break;
   }
   
   newString = String.substr(0, index);
   String.replace(0, index + 1, newString);
   
   if (String.at(index) != ' ') {
     numWords++;
   }
  } 
  return numWords;
}

/*(5)Implement FindText function that returns the number of instances
 a word or phrase is found in the string */
int FindText(string usrStr, string words) {
  
  string newString; 
  int index;
  int timesFound = 0;
  
  while(true) {
    
   index = words.find(usrStr);
   if (index == -1) {
     break;
   }
   
   timesFound++;
   
   newString = words.substr(0, index);
   words.replace(0, index + 1, newString);
   
  }
  return timesFound;
}

/*(6)Implement ReplaceExclamation function that updates the string by replacing each '!'
 character in the string with a '.' character. */
void ReplaceExclamation(string& words){
  string newString;
  int index;
  
  while(true){
    
    index = words.find("!");
    if (index == -1){
      break;
    }
    
    words.at(index) = '.';
  }
  return;
}

/*(7)Implement ShortenSpace function that updates the string by replacing all sequences
 of 2 or more spaces with a single space */
void ShortenSpace(string& words){
  string newString; 
  int index;
  
  while(true) {
    
   index = words.find("  ");
   if (index == -1) {
     break;
   }
   
   newString = words.substr(0, index);
   words.replace(0, index + 1, newString);
  }
  
  return;
}








//Ouputs the menu and implements the user's selection
char PrintMenu(string words){
  
  char answer;
  
  while (true){
    cout << "MENU" << endl;
    cout << "c - Number of non-whitespace characters" << endl;
    cout << "w - Number of words" << endl;
    cout << "f - Find text" << endl;
    cout << "r - Replace all !'s" << endl;
    cout << "s - Shorten spaces" << endl;
    cout << "q - Quit" << endl;
    cout << endl << "Choose an option:";
    cin >> answer; 
    cout << endl;
    
    switch(answer){
      
      case 'c':
        cout << "Number of non-whitespace characters: " << GetNumOfNonWSCharacters(words) << endl << endl;
        return answer;
        break;
        
      case 'w':
        cout << "Number of words: " << GetNumOfWords(words) << endl << endl;
        return answer;
        break;
      
      case 'f': //Placing braces around the case's statements create a scope for variables to be declared
        {
        string Text;
        cin.ignore(5, '\n');
        cout << "Enter a word or phrase to be found:";
        getline(cin, Text);
        cout << endl << "\"" << Text << "\"" << " instances: " << FindText(Text, words) << endl << endl;
        return answer;
        break;
        }
        
      case 'r':
        ReplaceExclamation(words);
        cout << "Edited text: " << words << endl << endl;
        return answer;
        break;
        
      case 's':
        ShortenSpace(words);
        cout << "Edited text: " << words << endl << endl;
        //statements fall through to case q
        
      case 'q':
        return answer;
        break;
      default:
        cout << endl << "INVALID CHOICE" << endl << endl;
    }
  }
  
}

/* Driver Program or main method */
int main() {
  
  string text;
  char answer;
  /*() 
  Prompt the user to enter a string  */
  cout << "Enter a sample text:"<<endl;
  /* Store a text */
  getline(cin, text);
  /* Output the sring */
  cout << endl << "You entered: " << text << endl << endl;
  
  while(true) {
    answer = PrintMenu(text);
    if (answer == 'q')
      break;
  } 
  return 0;
}