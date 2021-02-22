// coffee.cpp: Shows has-a relationships in C++ 
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Product {
    string name;
    int price;
    vector<string> recipe;
public:
    Product(const string& name, int price, const vector<string>& recipe)
        : name(name), recipe(recipe) 
    {
        this->price = price;
    }
    int get_price() const;
    void make() const;
};

class CashBox {
    int credit = 0;
    int total_cash = 0;
public:
    void deposit(int);
    int return_coins();
    bool have_you(int amount) const;
    void deduct(int amount);
    int total() const;
};

class Selector {
    CashBox* p_cash;
    vector<Product> products;
public:
    Selector(CashBox* p_cash, const vector<Product>& products) : products(products) {
        this->p_cash = p_cash;
    }
    void select(int choice);
};

class CoffeeMachine {
    CashBox* p_cash;
    Selector* p_selector;
public:
    CoffeeMachine() {
        p_cash = new CashBox;

        // Create Products
        vector<Product> products;
        products.emplace_back("black", 35, vector<string>{"cup","coffee","water"});
        products.emplace_back("white", 35, vector<string>{"cup","coffee","creamer","water"});
        products.emplace_back("sweet", 35, vector<string>{"cup","coffee","sugar","water"});
        products.emplace_back("white & sweet", 35, vector<string>{"cup","coffee","sugar","creamer","water"});
        products.emplace_back("bouillon", 5, vector<string>{"cup","bouillonPowder","water"});
        p_selector = new Selector(p_cash, products);
    }
    ~CoffeeMachine() {
        delete p_selector;
        delete p_cash;
    }
    bool one_action();
    double totalCash() const;
};