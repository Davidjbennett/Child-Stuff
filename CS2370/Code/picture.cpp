// picture.cpp: Shows Initialization in a class hierarchy (other methods not implemented)
#include <string>
using namespace std;

class Picture {
    string title;
    double price;
public:
    Picture(const string& title, double price) : title(title) {
        this->price = price;
    }
    void update_price(double);
};

class Photograph : public Picture {
    string photographer;
    string camera;
    double speed;
    double aperture;
public:
    Photograph(const string& title, double price, const string& photographer,
               const string& camera, double speed, double aperture)
        : Picture(title, price), photographer(photographer), camera(camera)
    {
        this->speed = speed;
        this->aperture = aperture;
    }
    void alter_contrast();
};

class Painting : public Picture {
    string artist;
    string type;
    string owner;
public:
    Painting(const string& title, double price, const string& artist,
               const string& type, const string& owner)
        : Picture(title, price), artist(artist), type(type), owner(owner)
    {}
    string print_provenance() const;
};