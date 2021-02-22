// stack3.cpp: Illustrates throwing exceptions
            
#include "stack2.h"         // No change to header file
#include <stdexcept>
using namespace std;

void Stack::push(int x) {
    data.push_back(x);
}

int Stack::pop() {
    if (data.size() == 0)
        throw length_error("underflow in pop");
    auto last = data.size() - 1;
    int x = data[last];
    data.resize(last);
    return x;
}

int Stack::top() const {
    if (data.size() == 0)
        throw length_error("underflow in top");
    return data[data.size() - 1];
}
int Stack::size() const {
    return data.size();
}
