#include <bits/stdc++.h>
using namespace std;

void readFile(string filename, vector<string> &loadWords)
{
    // open the file and read data word by word
    fstream file;
    string word;
    file.open(filename.c_str());

    // extracting words from file
    while (file >> word)
    {
        if (word[0] == '@')
        {
            string newFilename = word.erase(0, 1);
            // recursive call to itself with the new File name.
            readFile(newFilename, loadWords);
        }
        else
        {
            loadWords.push_back(word);
        }
    }
}

int main(int argc, char **argv)
{
    // a vector that contains all the words of the file
    vector<string> loadWords;
    
    cout << "32 items: " << endl << endl;

    // getting the command line arguments
    if (argc == 1)
    {
        cout << "#No command line arguments passed other than filename#\n";
    }
    else if (argc >= 2)
    {
        for (int i = 1; i < argc; i++)
        {
            // get the word (which can be a filename also)
            string word = argv[i];

            // if its a filename
            if (word[0] == '@')
            {
                // open the file and read the data recursively
                string fileName = word.erase(0, 1); // erases 1 char from 0th position (removes first letter)
                readFile(fileName, loadWords);
            }

            else
            {
                // put it inside the vector
                loadWords.push_back(word);
            }
        }
    }

    // print out all the words in the vector

    for (string word : loadWords)
    {
        cout << word << "\n";
    }

    return 0;
}