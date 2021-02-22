// fraction2.cpp: Illustrates operator overloading.

#include <cassert>
#include <iostream>
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
        assert(d != 0);
        int div = gcd(n, d);
        if (div > 1) {
            n /= div;
            d /= div;
        }
        num = n;
        den = d;
    }
    Fraction operator+(const Fraction& rhs) { 
        int new_num = num*rhs.den + rhs.num*den;
        int new_den = den*rhs.den;
        return Fraction(new_num, new_den); 
    }
    Fraction operator*(const Fraction& rhs) { 
        return Fraction(num*rhs.num, den*rhs.den);
    }
    friend ostream& operator<<(ostream&, const Fraction&);
};

ostream& operator<<(ostream& os, const Fraction& f) {
    os << f.num << '/' << f.den;
    return os;
}

int main() {
    Fraction f1(1, 2);
    Fraction f2(3, 4);
    cout << f1 + f2 << endl;    // operator<<(cout,f1.operator+(f2)).operator<<(endl);
    cout << f1 * f2 << endl;
    cout << f1 + 1 << endl;     // f1.operator+(Fraction(1))

    // The following won't compile:
    // cout << 1 + f1 << endl;  // 1.operator+(f1)???
}

/* Output:
5/4
3/8
3/2
*/
