// point3.h: Separate compilation for the Point class

// Include Guards:
#ifndef POINT3_H
#define POINT3_H

class Point {
    double x = 0, y = 0;
    Point diff(const Point& p2) const ;

public:
    Point() = default;  // To allow `Point p();`
    Point(double x, double y);

    // Accessors
    double get_x() const;
    double get_y() const;
    double distance(const Point& p2) const;
    double slope(const Point& p2) const;
};

#endif
