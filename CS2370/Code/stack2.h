// stack2.h: Header file for the Stack class
//           Contains only member function prototypes

#ifndef STACK2_H
#define STACK2_H

// No "#Include <iostream>"
#include <vector>
// Notice: No "using namespace std"

class Stack {
    std::vector<int> data;   // Notice std::
public:
    void push(int x);
    int pop();
    int top() const;
    int size() const;
};

#endif
