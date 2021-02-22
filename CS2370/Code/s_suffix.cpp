#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;

int main() {
    auto s1 = "Hello";
    cout << s1 << " is a " << typeid(s1).name() << endl;
    auto s2 = "Goodbye"s;
    cout << s2 << " is a " << typeid(s2).name() << endl;
}

/* Output from Visual Studio:
Hello is a char const *
Goodbye is a class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >
*/
