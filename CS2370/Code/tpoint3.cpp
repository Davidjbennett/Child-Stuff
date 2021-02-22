// tpoint3.cpp
#include "point3.h"
#include <iostream>
using namespace std;

int main() {
    Point p1(1,2);
    Point p2(3,4);
    cout << "Slope (p1,p2): " << p1.slope(p2) << endl;
    cout << "Distance (p1,p2): " << p1.distance(p2) << endl;

    Point origin;
    cout << "Slope (origin,p1): " << origin.slope(p1) << endl;
    cout << "Distance: " << origin.distance(p1) << endl;

    Point p3(p1);   // What is this?
    cout << "Slope (p2,p3): " << p2.slope(p3) << endl;
    cout << "Distance (p2,p3): " << p2.distance(p3) << endl;

    p3 = p2;
    cout << "Slope (p1,new p3): " << p1.slope(p3) << endl;
    cout << "Distance (p1, new p3): " << p1.distance(p3) << endl;
}

/* Output:
Slope (p1,p2): 1
Distance (p1,p2): 2.82843
Slope (origin,p1): 2
Distance: 2.23607
Slope (p2,p3): 1
Distance (p2,p3): 2.82843
Slope (p1,new p3): 1
Distance (p1, new p3): 2.82843
*/
