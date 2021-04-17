#ifndef SPLIT_H
#define SPLIT_H

#include <sstream>
#include <string>
#include <vector>

using std::istringstream;
using std::string;
using std::vector;

inline
vector<string> split(const string& s, char split_char) {
    istringstream iss(s);
    string buffer;
    vector<string> result;

    while (getline(iss, buffer, split_char))
        result.push_back(buffer);

    return result;
}

#endif
