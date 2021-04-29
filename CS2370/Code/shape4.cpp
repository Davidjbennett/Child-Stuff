// shape4.cpp: Illustrates how passing objects as parameters
// affects polymorphism.

#include <cmath>
#include <iostream>
#include <sstream>
using namespace std;

const double PI = 3.141592653;

class Shape {
    inline static int next_id = 1;
    int id;

public:
    Shape() {
        id = next_id++;
    }
    int getID() const {
        return id;
    }
    // The following functions have been changed
    virtual double area() const {
        return 0.0;
    }
    virtual string to_string() const {
        ostringstream oss;
        oss << "Shape(id=" << id << ')';
        return oss.str();
    }
};

class Circle : public Shape {
    double radius;
public:
    Circle(int rad) {
        radius = rad;
    }
    double area() const override {
        return PI*radius*radius;
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Circle(id=" << getID() << ", radius=" << radius << ')';
        return oss.str();
    }
};

class Rectangle : public Shape {
    double length;
    double width;
public:
    Rectangle(int len, int wid) {
        length = len;
        width = wid;
    }
    double area() const override {
        return length*width;
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Rectangle(id=" << getID() << ", length=" 
            << length << ", width=" << width << ')';
        return oss.str();
    }
};

class Triangle : public Shape {
    double side_1;
    double side_2;
    double side_3;
public:
    Triangle(double s1, double s2, double s3) {
        side_1 = s1;
        side_2 = s2;
        side_3 = s3;
    }
    double area() const override {
        double s = (side_1 + side_2 + side_3) / 2.0;
        return sqrt(s*(s-side_1)*(s-side_2)*(s-side_3));
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Triangle(id=" << getID() << ", s1=" << side_1 
            << ", s2=" << side_2 << ", s3=" << side_3 << ')';
        return oss.str();
    }
};

// No polymorphism for display1; only the Shape subobject is passed (sliced)
void display1(Shape s) {
    cout << s.to_string() << endl;
}

// The next 2 functions ARE polymorphic
void display2(const Shape& s) {
    cout << s.to_string() << endl;
}

void display3(const Shape* p) {
    cout << p->to_string() << endl;
}

int main() {
    Circle c1(3.0); display1(c1); display2(c1); display3(&c1);
    Circle c2(4.0); display1(c2); display2(c2); display3(&c2);
    Rectangle r(20, 30); display1(r); display2(r); display3(&r);
    Triangle t(20, 30, 40); display1(t); display2(t); display3(&t);

}

/* Output:
Shape
Circle(id=1, radius=3)
Circle(id=1, radius=3)
Shape
Circle(id=2, radius=4)
Circle(id=2, radius=4)
Shape
Rectangle(id=3, length=20, width=30)
Rectangle(id=3, length=20, width=30)
Shape
Triangle(id=4, s1=20, s2=30, s3=40)
Triangle(id=4, s1=20, s2=30, s3=40)
*/
