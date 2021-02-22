// fraction.cpp: Holds a numerator and denominator
//               Supports fraction arithmetic.
//               Here we assume all numbers are non-negative.
//               Here gcd is a static helper function, but 
//               helper functions can also be non-static as well.

#include <cassert>
#include <iostream>
using namespace std;

class Fraction {
    // Private members
    int num;
    int den;
    static int gcd(int m, int n) {
        // Greatest common divisor (Euclid's algorithm)
        // Principle: gcd(m, n) == gcd(n, m % n)
        // Repeat until you get 0. The previous result is the gcd
        return (n == 0) ? m : gcd(n, m%n);
    }
public:
    Fraction(int n = 0, int d = 1) {
        assert(d != 0);         // Zero denominator not allowed
        int div = gcd(n, d);    // Find gcd to reduce to lowest terms
        if (div > 1) {
            n /= div;
            d /= div;
        }
        num = n;
        den = d;
    }
    Fraction add(const Fraction& rhs) {     // *this* is the lhs
        int new_num = num*rhs.den + rhs.num*den;
        int new_den = den*rhs.den;
        return Fraction(new_num, new_den);  // Constructor call
    }
    Fraction mult(const Fraction& rhs) { 
        return Fraction(num*rhs.num, den*rhs.den);
    }
    void display() const {
        cout << num << '/' << den << endl;
    }
};

int main() {
    Fraction f1(1, 2);
    Fraction f2(3, 4);
    Fraction sum = f1.add(f2);
    sum.display();
    Fraction prod = f1.mult(f2);
    prod.display();

    Fraction f3(5);     // 5/1
    Fraction zero;      // 0/1
    sum = f3.add(zero);
    sum.display();
    prod = f3.mult(zero);
    prod.display();
}

/* Output:
5/4
3/8
5/1
0/1
*/
