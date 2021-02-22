// stack2.cpp: Illustrates out-of-class function bodies
//            
#include "stack2.h"         // Include class header file (has class definition)
#include <cassert>          // #include stack2.h before standard headers in this file
using namespace std;        // Okay to put this in a .cpp file

void Stack::push(int x) {
    data.push_back(x);
}

int Stack::pop() {
    assert(data.size() > 0);
    auto last = data.size() - 1;
    int x = data[last];
    data.resize(last);
    return x;
}

int Stack::top() const {
    assert(data.size() > 0);
    return data[data.size() - 1];
}
int Stack::size() const {
    return data.size();
}
