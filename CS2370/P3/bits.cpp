#ifndef BITS_H
#define BITS_H 

#include <bitset>
#include <cassert>
#include <iostream>

using namespace std;

class Bits {
    using IType = unsigned long long;
    enum {NBITS = sizeof(IType)*8};
    IType bits = 0; // This is the only data in a Bits object
public:
    Bits(IType n=0) {
        bits = n;
    }
    static int size() {
        return NBITS;
    }
    //! TODO:
    bool at(int pos) const {
        assert(0 <= pos && pos < NBITS);
        // return the bit in position `pos`
        IType mask = (1 << pos);
        IType result = (bits & mask);
        if(result == mask){
            return true;
        } else{
            return false;
        }
    }

    //! DONE
    void set(int pos) {
        assert(0 <= pos && pos < NBITS);
        // set the bit in position `pos`
        IType num = (1 << pos);
        bits |= num;
    }
    void set() {
        bits = IType(-1);
    }

    //! DONE
    void reset(int pos) {
        assert(0 <= pos && pos < NBITS);
        // return the bit in position `pos`
        IType num = ~(1 << pos);
        bits &= num;
    }
    void reset() {
        bits = 0;
    }

    //! DONE
    void assign(int pos, bool val) {
        assert(0 <= pos && pos < NBITS);
        // set or reset the bit in position `pos`
        if(val){
            IType num = (1 << pos);
            bits |= num;    
        }else{
            IType num = ~(1 << pos);
            bits &= num;
        }
    }
    void assign(IType n) {
        bits = n;
    }

    //! DONE
    void toggle(int pos) {
        assert(0 <= pos && pos < NBITS);
        // toggle the bit in position `pos`
        if(at(pos) == 1){
            reset(pos);
        }else{
            set(pos);
        }
    }
    void toggle() {
        bits = ~bits;
    }

    //! DONE
    void shift(int n) {
        if (n > 0)
            bits = bits >> n;
            // Shift right n
        else if (n < 0)
            bits = bits << -(n);
        // Shift left -n (n is negative, so -n is positive)
        // Ignore a 0-shift
    }

    //! DONE:
    void rotate(int n) {
        assert(abs(n) <= NBITS);
        /*Shift bits which way and store new bits in var
        get bits that fell off in a new var
        or the two vars together*/
        if (n > 0) {
            // Rotate right
            IType mask = (1 << n)-1;
            IType temp = mask & bits;
            shift(n);
            temp <<= NBITS-n;
            bits |= temp;
            
        }
        else if (n < 0) {
            // Rotate left (n is negative!)
            IType mask = (1 << (-n))-1;
            mask <<= NBITS-(-n);
            IType temp = mask & bits;
            shift(n);
            temp >>= NBITS-(-n);
            bits |= temp;
        }
    }

    //! DONE:
    int ones() const {
        int count = 0;
        // for(int i = 0; i < NBITS; i++){
        //     int pos = at(i);
        //     if(pos == 1){
        //         count++;
        //     }
        // }
        IType numBit = bits;
        IType mask = 1;
        for (int i = 0; i < NBITS; i++){
            int result = numBit & mask;
            numBit >>= 1;
            if(result == 1){
                count++;
            }
        }
        
        return count;
        // Count the number of 1's
        // Let n = bits.
        // And the number with 1
        // Then, shift n to the right, repeat...
    }

    //! ALL BELOW DONE
    int zeroes() const {
        return NBITS - ones();
    }
    IType to_int() const {
        return bits;
    }
    friend bool operator==(const Bits& b1, const Bits& b2) {
        return b1.bits == b2.bits;
    }
    friend bool operator!=(const Bits& b1, const Bits& b2) {
        return b1.bits != b2.bits;
    }
    friend std::ostream& operator<<(std::ostream& os, const Bits& b) {
        return os << std::bitset<NBITS>(b.bits);
    }
};

#endif

// using namespace std;

int main() {
    // Bits mask(155);
    // cout << mask << endl;
    // mask.rotate(-30);
    // cout << mask << endl;



    // unsigned long long mask = 0;
    // mask = (1 << 3)-1;
    // cout << bitset<64>(mask) << endl;
    // mask <<= 64-3;

    // cout << bitset<64>(mask) << endl;
    // cout << mask;

  Bits a(155155155155155);
  cout << a << endl;
  cout << a.at(32) << endl;
  cout << a.at(33) << endl;
  cout << a.at(34) << endl;
  cout << a.at(35) << endl;
  cout << a.at(36) << endl;
  cout << a.at(37) << endl;
  cout << a.at(38) << endl;
  cout << a.at(39) << endl;
  cout << a.at(40) << endl;
//   cout << a.ones();

//   cout << bitset<64>(a.to_int()) << endl;

  /*Completed:
  at
  set
  reset
  shift
  assign
  toggle
  */
}
