// fraction4.cpp: Illustrates exception handling, replacing asserts.
//                Use logic_error for preventable, programmer errors.
//                Use asserts for debugging your own code (your errors).
//                Use runtime_error for user errors.

#include <iostream>
#include <stdexcept>    // Standard exception classes defined here
using namespace std;

class Fraction {
    // Private members
    int num;
    int den;
    static int gcd(int m, int n) {
        return (n == 0) ? m : gcd(n, m%n);
    }
public:
    Fraction(int n = 0, int d = 1) {
        if (d == 0)
            throw invalid_argument("zero denominator not allowed");
        int div = gcd(abs(n), abs(d));
        if (div > 1) {
            n /= div;
            d /= div;
        }
        num = n;
        den = d;
    }
    friend Fraction operator+(const Fraction& lhs, const Fraction& rhs) { 
        int new_num = lhs.num*rhs.den + rhs.num*lhs.den;
        int new_den = lhs.den*rhs.den;
        return Fraction(new_num, new_den); 
    }
    friend Fraction operator*(const Fraction& lhs, const Fraction& rhs) { 
        return Fraction(lhs.num*rhs.num, lhs.den*rhs.den);
    }
    friend ostream& operator<<(ostream& os, const Fraction& f) {
        os << f.num << '/' << f.den;
        return os;
    }
};

int main() {
    Fraction f1(1, 2);
    Fraction f2(3, 4);
    cout << f1 + f2 << endl;
    cout << f1 * f2 << endl;
    cout << f1 + 1 << endl;
    cout << 1 + f1 << endl;

    // Test exception handling
    try {
        Fraction f3(1, 0);
    }
    catch (logic_error& exc) {      // invalid_argument is-a logic_error
        cout << exc.what() << endl;
    }
}

/* Output:
5/4
3/8
3/2
3/2
zero denominator not allowed
*/
