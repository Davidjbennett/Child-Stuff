/*
6.5 LAB: Exception handling to detect input string vs. int The 
given program reads a list of single-word first names and ages 
(ending with -1), and outputs that list with the age incremented. 
The program fails and throws an exception if the second input on a 
line is a string rather than an int. At FIXME in the code, add a 
try/catch statement to catch ios_base::failure, and output 0 for 
the age. Ex: If the input is: Lee 18 Lua 21 Mary Beth 19 Stu 33 -1 
then the output is: Lee 19 Lua 22 Mary 0 Stu 34
*/

#include <string>
#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
   string inputName;
   int age;
   // Set exception mask for cin stream
   cin.exceptions(ios::failbit);

   cin >> inputName;
    while(inputName!="-1"){
        try{
        cin>>age;
        }
        catch (ios_base::failure &) {
            string temp;
            cin.clear();
            cout<<inputName<<" "<<(age)<<endl; 
            cin>>temp;
            cin>>temp;
            cin>>inputName;
            continue;
        }
    cout<<inputName<<" "<<(age+1)<<endl;
    cin>>inputName;
   }
return 0;
}