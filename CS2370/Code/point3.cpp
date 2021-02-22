// point3.cpp: Separte compilatiuon implementation bodies

#include "point3.h"
#include <cmath>
using namespace std;

Point Point::diff(const Point& p2) const {
    return Point(p2.x - x, p2.y - y);
}

Point::Point(double x, double y) {
    this->x = x;
    this->y = y;
}

// Accessors
double Point::get_x() const {
    return x;
}
double Point::get_y() const {
    return y;
}
double Point::distance(const Point& p2) const {
    auto [x_dist, y_dist] = diff(p2);
    return sqrt(x_dist*x_dist + y_dist*y_dist);
}
double Point::slope(const Point& p2) const {
    auto [x_dist, y_dist] = diff(p2);
    return y_dist / x_dist;
}

