// argv.cpp
#include <cstddef>
#include <cstring>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {      // char** argv
    for (int i = 0; i < argc; ++i) {
        size_t length = strlen(argv[i]);
        for (int j = 0; j < length; ++j)
            cout << argv[i][j] << ' ';  // *(*(argv + i) + j)
        cout << endl;
    }     
}

/*
(a+i) == a[i], therefore...
argv[i][j] == *(*(argv + i) + j)

Sample execution:
$ ./a.out one two
. / a . o u t 
o n e 
t w o 
*/
