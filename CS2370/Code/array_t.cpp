// array_t.cpp: A safe array class template
// 
// Note that by having a begin/end pair of methods enables using a 
// range-based for loop!
// 
// Not also that the array is not passed as a pointer to the first element.
// Finally, note that we don't have to manage memory. Like built-in arrays,
// this class is statically sized.

#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

template<typename T, size_t N>
class Array {
    T data[N] = {};      // Default initialization (even for built-ins!)
public:
    T get(size_t pos) const {
        if (pos >= N)
            throw range_error("Index out of range.");
        return data[pos];
    }  
    void set(size_t pos, const T& t) {
        if (pos >= N)
            throw range_error("Index out of range.");
        data[pos] = t;
    }
    size_t size() const {
        return N;
    }
    T* begin() {
        return data;
    } 
    T* end() {
        return data+N;
    } 
};

template<typename T, size_t N>
void print_array(Array<T,N>& arr) {   // Array<T,N> is a type
    cout << N << " elements of type " << typeid(T).name() << " occupy " 
         << sizeof(arr) << " bytes\n";
    for (auto& elem: arr) 
        cout << elem << ' ';
    cout << endl;
}

int main() {
    // Hold ints
    Array<int, 5> a;
    cout << sizeof(a) << endl;  // 20
    print_array(a);

    for (size_t i = 0; i < a.size(); ++i)
        a.set(i, int(i+1));
    print_array(a);

    a.set(3, 99);
    cout << a.get(3) << endl;   // 99

    // Hold strings
    Array<string, 5> s;
    for (const string& t: s)
        cout << '"' << t << "\" ";  // "" "" "" "" "" 
    cout << endl;

    for (size_t i = 0; i < s.size(); ++i)
        s.set(i, to_string(i+1));
    for (const string& t: s)
        cout << '"' << t << "\" ";  // "1" "2" "3" "4" "5" 
    cout << endl;

    s.set(3, "99");
    cout << '"' << s.get(3) << "\"" << endl; // "99"
}

/* Output:
20
5 elements of type i occupy 20 bytes
0 0 0 0 0 
5 elements of type i occupy 20 bytes
1 2 3 4 5 
99
"" "" "" "" "" 
"1" "2" "3" "4" "5" 
"99"
*/
