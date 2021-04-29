// shape7.cpp: Illustrates vector of unique_ptrs, for automatic memory mgt!

#include <cmath>
#include <iostream>
#include <memory>
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
    virtual ~Shape(){cout << "~Shape()\n";}     // or `virtual ~Shape() = default;`
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
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(unique_ptr<Shape>(new Circle(3.0)));
    shapes.emplace_back(new Circle(4.0));
    shapes.emplace_back(new Rectangle(20,30));
    shapes.emplace_back(new Triangle(20,30,40));

    shapes.pop_back();  // Remove Triangle first
}

/* Output:
~Triangle()
~Shape()
~Rectangle()
~Shape()
~Circle()
~Shape()
~Circle()
~Shape()
*/
