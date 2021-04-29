// shape6.cpp: Illustrates virtual destructors. Remove virtual to see the difference.

#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

const double PI = 3.141592653;

class Shape {
    inline static int next_id = 1;

protected:
    const int id;

public:
    Shape() : id(next_id++) {}
    virtual ~Shape(){cout << "~Shape()\n";}     // Try with and without virtual
    int getID() const {
        return id;
    }
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
    virtual ~Circle(){cout << "~Circle()\n";}
    double area() const override {
        return PI*radius*radius;
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Circle(id=" << id << ", radius=" << radius << ')';
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
    virtual ~Rectangle(){cout << "~Rectangle()\n";}
    double area() const override {
        return length*width;
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Rectangle(id=" << id << ", length=" 
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
    virtual ~Triangle(){cout << "~Triangle()\n";}
    double area() const override {
        double s = (side_1 + side_2 + side_3) / 2.0;
        return sqrt(s*(s-side_1)*(s-side_2)*(s-side_3));
    }
    string to_string() const override {
        ostringstream oss;
        oss << "Triangle(id=" << id << ", s1=" << side_1 
            << ", s2=" << side_2 << ", s3=" << side_3 << ')';
        return oss.str();
    }
};

int main() {
    vector<Shape*> shapes{new Circle(3.0), new Circle(4.0), new Rectangle(20,30), 
                          new Triangle(20,30,40)};
    for (const Shape* p: shapes)
        cout << p->to_string() << endl;

    // Freeing memory leaves deleted pointers in the vector!
    for (Shape* p: shapes)
        delete p;

    // So we better do this immediately!
    shapes.clear();
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
