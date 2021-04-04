#include "Vector.h"
#include "test.h"
#include <stdexcept>
#include <Vector>
using namespace std;

int main() {
    // Test exceptions
    Vector v;
    throw_(v.at(0), range_error);
    throw_(v.pop_back(), range_error);
    throw_(v.erase(0), range_error);
    throw_(v.front(), range_error);
    throw_(v.back(), range_error);

    // Test adding an element
    v.push_back(1);
    test_(v.size() == 1);
    test_(v.at(0) == 1);
    test_(v[0] == 1);
    test_(v.front() == 1);
    test_(v.back() == 1);
    test_(!v.empty());

    // Add another
    v.push_back(2);
    test_(v.size() == 2);
    test_(v.at(0) == 1);
    test_(v.at(1) == 2);
    test_(v[0] == 1);
    test_(v[1] == 2);
    test_(v.front() == 1);
    test_(v.back() == 2);
    test_(!v.empty());

    // Test iterators
    auto iter = v.begin();
    test_(*iter == 1);
    ++iter;
    test_(*iter == 2);
    ++iter;
    test_(iter == v.end());

    // Test copy and ==
    Vector v2 = v;
    test_(v2.size() == 2);
    test_(v2.at(0) == 1);
    test_(v2.at(1) == 2);
    test_(v2[0] == 1);
    test_(v2[1] == 2);
    test_(v2.front() == 1);
    test_(v2.back() == 2);
    test_(!v2.empty());
    test_(v == v2);

    iter = v2.begin();
    test_(*iter == 1);
    ++iter;
    test_(*iter == 2);
    ++iter;
    test_(iter == v2.end());

    // Test assignment
    Vector v3;
    v3 = v;
    test_(v3.size() == 2);
    test_(v3.at(0) == 1);
    test_(v3.at(1) == 2);
    test_(v3[0] == 1);
    test_(v3[1] == 2);
    test_(v3.front() == 1);
    test_(v3.back() == 2);
    test_(!v3.empty());

    iter = v3.begin();
    test_(*iter == 1);
    ++iter;
    test_(*iter == 2);
    ++iter;
    test_(iter == v3.end());

    // Test assignment
    v[1] = -2;
    test_(v.back() == -2);
    test_(v.at(1) == -2);
    test_(v[1] == -2);

    // Test pop_back
    v.pop_back();
    test_(v.size() == 1);
    test_(v.front() == 1);
    test_(v.back() == 1);
    test_(v.at(0) == 1);
    test_(v[0] == 1);

    // Test clear and !=
    v.clear();
    test_(v.size() == 0);
    test_(v.empty());
    throw_(v.at(0), range_error);
    throw_(v.pop_back(), range_error);
    throw_(v.erase(0), range_error);
    throw_(v.front(), range_error);
    throw_(v.back(), range_error);
    test_(v != v2);

    // Test erase
    v3.erase(0);
    test_(v3.size() == 1);
    test_(v3.at(0) == 2);
    test_(v3[0] == 2);
    test_(v3.front() == 2);
    test_(v3.back() == 2);

    // Test insert
    v3.insert(0,1);
    test_(v3.size() == 2);
    test_(v3.at(0) == 1);
    test_(v3[0] == 1);
    test_(v3[1] == 2);
    test_(v3.front() == 1);
    test_(v3.back() == 2);

    // Test grow
    Vector v4;
    for (int i = 1; i <= 10; ++i)
        v4.push_back(i);
    test_(v4.size() == 10);
    test_(v4.front() == 1);
    test_(v4.back() == 10);
    v4.insert(10,11);
    test_(v4.size() == 11);
    test_(v4.front() == 1);
    test_(v4.back() == 11);


    report_();
}