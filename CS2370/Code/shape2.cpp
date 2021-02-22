// shape2.cpp: Comment-out an override and see what happens.
#include <cmath>
#include <iostream>
#include <sstream>
using namespace std;

const double PI = 3.141592653;

class Shape {
    int id;
    inline static int next_id = 0;
public:
    Shape() {
        id = ++next_id;
    }
    int getID() const {
        return id;
    }
    virtual double area() const = 0;  // No body needed
    virtual string to_string() const = 0;
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

int main() {
    Circle c1(3.0);
    cout << c1.to_string() << ", area=" << c1.area() << endl;

    Circle c2(4.0);
    cout << c2.to_string() << ", area=" << c2.area() << endl;

    Rectangle r(20, 30);
    cout << r.to_string() << ", area=" << r.area() << endl;

    Triangle t(20, 30, 40);
    cout << t.to_string() << ", area=" << t.area() << endl;
}

/* Output:
Circle(id=1, radius=3), area=28.2743
Circle(id=2, radius=4), area=50.2655
Rectangle(id=3, length=20, width=30), area=600
Triangle(id=4, s1=20, s2=30, s3=40), area=290.474
*/
