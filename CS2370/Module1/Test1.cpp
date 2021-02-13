// ! floating-point numbers, literals ("E10"), don't compare for equality
// ! % operator
// ! ++, --
// ! >> (input operator) skips whitespace
// ! boolean operators, short-circuit, &&, ||, ! if (5 || false), !!
// ! truthy = true, non-zero; falsy = false, 0
// ! For integers: !!truthy == 1, !!falsy == 0
// ! cout << boolalpha to print "false" instead of 0, "true" instead of 1
// ! switch statement
// ! conditional operator
// ! loops (while, do-while, for (init; cond; cycle), range-based for (auto x: sequence))
// ! bitwise operators (<<, >>, ~, |, &, ^)
// ! prefer unsigned integers when using bitwise operators
// ! vector, init., at() vs. [], push_back, pop_back, size(), begin(), end()
// ! arrays, init, arrays as parameters, multi-dimensional arrays
// ! C-style strings, '\0', literals have the '\0' included, <cctype> functions
// ! functions, pass by value, pass by reference, const, default args, overloading
// ! stack frames
// ! local static variables (not on stack)
// ! recursion, binary search
// ! <> vs. "" in #include; header guards
// ! scope and shadowing
// ! enums

#include <cmath>
#include <iostream>
#include <string>
#include <bitset>
#include <vector>
using namespace std;

int main(){
    //! floating point  numss
    double x = sqrt(2.0);
    cout.precision(20); //! have to set precision for it to return
                        //! specific length of digits
    cout << fixed << x << endl;
    cout << boolalpha << (x == 1.41421356237309514547) << endl;
    //! spits out true until number is 1.414213562373095 then its false
    cout << (abs(x - 1.414213562373095) < 1.0e-10) << endl; //! ask if diff
    //! between x and 1.414213562373095 is less than .0000000001 (this num specifies precision)


    //! modulus
    int n = 10;
    for(int i = 2; i <=10; i++){
        cout << n%i << endl;
        //! output: 0,1,2,0,4,3,2,1,0
    }


    //!increment decrement operators
    int x=1, y=2;
    int z = x++ + ++y; //! x increments after z is equaled to x and y+1
    cout << x << ', ' << y << ', ' << z << endl; 
    //!prints out 2, 3, 4


    // int n = 0;
    // while (f >> x){ //!  >>  always skips whitespace (tabs, ' ', newlines)
    //     a[n++] = x;
    // }
    

    //! getline(cin, x) collects everything up to a newline
    //! getline(cin, x, '$') collects everything up to a dollar sign

    //! && is logical 'and' and & is bitwise 'and'

    cout << boolalpha << bool(2.0) << ',' << bool(0.0) << endl;
    //! cout << bool(string("")) << ',' << bool(string("1")) << endl;
    //! 2nd line cant convert string to bool

    cout << !5 << endl; //! returns 0
    cout << !0 << endl; //! returns 1
    //! sticking in << boolalpha prints out true or false instead of 1 or 0


    cout << boolalpha << (5 || 1/0) << endl;
    //! 5 is true and 1/0 returns true
    //! 5 && 1/0 returns false

    int n = 5;
    cout << boolalpha << !(!n) << endl;
    //! prints out true
    //! 5 is true, !5 is false, !!5 is true

    cout << "enter a num" << endl;
    int n;
    cin >> n;
    switch (n){
    case 1:
        cout << "Some words" << endl;
        break;
    case 2:
        cout << "2 huh??" << endl;
        break;
    default:
        cout << "chump didnt get it right" << endl;
        break;
    }


    //! conditional operator
    //! condition ? true-val : false-val
    //! reads: if condition is true return true-val else return false-val
    //! returns need to be same type. cant return 1 and a string. you can
    //! return int and float tho

    //! fibonacci in 2 lines
    /*
    int fib(int n){
        assert(n >= 0)
        return (n == 0 || n==1) ? n : fib(n-1) + fib(n-2);
    }
    */


    //!loops (while, do-while, for)
    //! do while runs the loop atleast once checks after code is run
    //! while loop checks input at start
    //! for(initialize counter; condition; incrememnt counter)
    //! range based for (auto x: sequence) arrays must be in the same scope
    //! youre using range based for on. You can pass vectors into functions
    //! that use ranged base for for vectors, but not arrays


    //! bitwise operators (<<, >>, ~, |, &, ^)
    // << shifts left
    // >> shifts right
    // ~ bitwise not
    // | bitwise or
    // & bitwise and
    // ^ bitwise exclusive or
    //! short is 16 bits int is 64
    unsigned short n = 11; //0000...1011
    unsigned short mask = 1; // 000...0001
    cout << bitset<16>(n) << endl; // gives 16 bit representation of 11
    for (unsigned int i = 0; i <= 16; ++i){
        cout << bitset<16>(n<<i) << endl;
        //! prints out 17 lines each shifted left once
    }
    cout << boolalpha << (n & (mask << 3)) << endl;
    n |= (mask << 2); //! uses an or equals
    cout << n << endl; // prints 15 or 1111
    n &= ~(mask << 2); //! uses an and equals
    cout << n << endl; // prints 11 or 1011
    n ^= 0b1100; //! uses an exclusive or
    cout << n << endl; // prints 7 or 0111


    //! vectors
    vector<int> v; //empty vector
    vector<int> v = {1,2,3}; // vector with a size of 3
    cout << v[1] << endl; // prints element 1
    cout << v.at(1) << endl; // does same thing, but .at() checks bounds
    //! functions: pop_back(), push_back(), size(), begin(), end()
    for (auto p = begin(v); p != end(v); ++p){ // begin gives pointer to first element
        cout << *p << endl; // * says give me value through pointer
    }

    for(auto val: v){ //rangd baed for loop
        cout << val << endl;
    }


    //! arrays
    int a[] = {1,2,3};
    for (auto val: a){ //! ranged based only works bc array is in same scope
        cout << val << endl;
    }

    /* //! passed by reference with &. This avoids copying values
    ! const keeps it from being changed.
    ! int a[], int n passes in an array of elements. cant use ranged base for
    ! with it passed in array.
    void display(const vector<int>& v){ 
        for(auto val: v){
            cout << val << endl;
        }
    }
    */

   //! multi dimensional arrays
    int a[][3] = {{1,2,3}, {4,5,6}};
    cout << sizeof(a[0]) << endl;
    for (auto& row: a){
        for (int n: row){
           cout << n << ' ';
       } 
       cout << endl;
   }

}
