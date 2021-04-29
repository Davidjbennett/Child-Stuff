#include <set>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <random>
#include <ctime>
#include <algorithm>

using namespace std;
vector<string> words;

void subWords(string& random_word){
    vector<string> word_subsets;

    multiset<char> m1{begin(random_word), end(random_word)};
    for (string &s : words){
        multiset<char> m2{begin(s), end(s)};
        bool is_subset = includes(begin(m1),end(m1), begin(m2), end(m2));
        if (is_subset == true && s.length() > 2){
            word_subsets.push_back(s);
        }
    }

    int size = 3;
    for (int i = 3; i <= random_word.length(); i ++){
        vector<string> one_size;
        for (auto x : word_subsets){
            if(x.size() == size){
                one_size.push_back(x);
            }
        }
        sort(one_size.begin(), one_size.end());
        for(auto x : one_size){
            cout << x << endl;
        }
        size++;
    }
}

int main(){
    ifstream ifs("D:\\UVU\\DavidBennett\\CS2370\\P6\\words.txt");
    //! The above is the file location on my pc
    // ifstream ifs("words.txt");
    string word = "";
    while (ifs >> word){
        words.push_back(word);
    }

    default_random_engine dre(time(nullptr));
    uniform_int_distribution<int> di(0, words.size());
    int n = di(dre);
    string random_word = words.at(n);
    subWords(random_word);
}