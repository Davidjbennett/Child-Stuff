// shape3.cpp: Wants an array of Shapes. Must use pointers. 
// Shape can't be instantiated. Even if it could, you can't
// put different-sized objects in a single array!

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
    Circle c2(4.0);
    Rectangle r(20, 30);
    Triangle t(20, 30, 40);

    // Object sizes:
    cout << "sizeof(Shape) = " << sizeof(Shape) << endl;            // 16
    cout << "sizeof(Circle) = " << sizeof(Circle) << endl;          // 24
    cout << "sizeof(Rectangle) = " << sizeof(Rectangle) << endl;    // 32
    cout << "sizeof(Triangle) = " << sizeof(Triangle) << endl;      // 40

    // Error:
//  Shape shapes[] = {c1, c2, r, t};

    Shape* shapes[] = {&c1, &c2, &r, &t};
    for (Shape* ptr: shapes) 
        cout << ptr->to_string() << endl;   // Polymorphism!   
}

/* Output:
sizeof(Shape) = 16
sizeof(Circle) = 24
sizeof(Rectangle) = 32
sizeof(Triangle) = 40
Circle(id=1, radius=3)
Circle(id=2, radius=4)
Rectangle(id=3, length=20, width=30)
Triangle(id=4, s1=20, s2=30, s3=40)
*/
