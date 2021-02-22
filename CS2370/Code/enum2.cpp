// Scoped enums
#include <iostream>
using namespace std;

enum class Color {red, green, blue};

void display_color(Color c) {
    switch(c) {
        case Color::red:
            cout << "red\n";
            break;
        case Color::green:
            cout << "green\n";
            break;
        case Color::blue:
            cout << "blue\n";
            break;
    }
}

int main() {
    Color c = Color::red;
    display_color(c);       // red
}