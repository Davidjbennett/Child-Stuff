// point.cpp: A simple point class, holding x,y coordinates.
// Note: This class has no setters. Otherwise we could use a struct.
// Therefore, all methods are const.

// Structured bindings are illustrated in distance() and slope().

#include <cmath>
#include <iostream>
using namespace std;

class Point {
    double x, y;
    // Re-using Point here as a container for returning two numbers.
    // See the corresponding structured bindings in distance() and slope().
    Point diff(const Point& p2) const {
        return Point(p2.x - x, p2.y - y);
    }

public:
    // Three contructors in one!
    Point(double x = 0.0, double y = 0.0) {
        this->x = x;
        this->y = y;
    }

    // Accessors
    double get_x() const {
        return x;
    }
    double get_y() const {
        return y;
    }
    double distance(const Point& p2) const {
        auto [x_dist, y_dist] = diff(p2);   // Structured binding
        return sqrt(x_dist*x_dist + y_dist*y_dist);
    }
    double slope(const Point& p2) const {
        auto [x_dist, y_dist] = diff(p2);   // Structured binding
        return y_dist / x_dist;
    }
};

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
