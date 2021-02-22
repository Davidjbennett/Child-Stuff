// scope.cpp: The use of i below is not good practice!
#include <iostream>
using namespace std;

int i = 10;                 // global variable

void f() {
    cout << i << endl;
}

namespace Foo {
    int i = 40;
}

int main()
{
   cout << i << endl;

   int i = 20;              // i local to main
   cout << i << endl;

   // Creating an arbitrary scope
   {    
      int i = 30;
      cout << i << endl;    // This inner i (30)
      cout << ::i << endl;  // The global i (10)
   }
   cout << i << endl;       // 20
   f();                     // 10
   cout << Foo::i << endl;
}

/* Output:
10
20
30
10
20
10
40
*/

