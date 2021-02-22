// init1.cpp: Shows how a default constructor is used by default.
//            In this example, it is missing, so there is a compiler error.

#include <string>

class Part {
    int n;
public:
    Part(int n) {
        this->n = n;
    }
};

class Whole {
    std::string s;
    Part p;
public:
};

int main() {
    Whole w;
}

/* Compile Error:
/Users/chuck/Desktop/UVU/2370/Code/init1.cpp:21:11: error: call to implicitly-deleted default constructor of 'Whole'
    Whole w;
          ^
/Users/chuck/Desktop/UVU/2370/Code/init1.cpp:16:10: note: default constructor of 'Whole' is implicitly deleted because field 'p' has no default constructor
    Part p;
         ^
1 error generated.
*/
