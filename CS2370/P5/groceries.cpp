#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "split.h"
using namespace std;



//!TODO: print_detail()
class Customer{
    int cust_id;
    string name;
    string street;
    string city;
    string state;
    string zip;
    string phone;
    string email;

public:
    Customer(int cust_id, const string& name, const string& street, const string& city, 
            const string& state, const string& zip, const string& phone, 
            const string& email) : name(name), street(street), city(city), state(state), 
            zip(zip), phone(phone), email(email){
                 this->cust_id = cust_id;
             }
    string print_detail(){
        return this->name;
    };
};

//!TODO:
class LineItem{
    int item_id;
    int qty;

public:
    LineItem(int item_id, int qty){
        this->item_id = item_id;
        this->qty = qty;
    }
    // double sub_total(){
    //     return this->qty * ;
    // }
};

//!DONE
class Item{
    int item_id;
    string description;
    double price;
public:
    Item(int id, const string& desc, double price) : description(desc){
        this->item_id = id;
        this->price = price;
    }
    int get_id(){
        return this->item_id;
    }
    string get_desc(){
        return this->description;
    }
    double get_price(){
        return this->price;
    }
};

//!TODO:
class Payment{
    double amount;
public:
    virtual string print_detail();
};

//!TODO:
class Credit{
    string card_number;
    string expiration;
public:
    string print_detail();
};

//!TODO:
class PayPal{
    string paypal_id;
public:

};

//!TODO:
class WireTransfer{
    string bank_id;
    string account_id;
public:

};

//!TODO:
class Order {
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;

public:
    double total();
    string print_order();
};

//! Globals
vector<Item> items;
vector<Customer> customers;
vector<Order> orders;

//!DONE
void read_customers(const string& fname2){
    string line;
    ifstream f(fname2);

    while (getline(f, line)){
        auto cust = split(line, ',');
        customers.emplace_back(stoi(cust[0]), cust[1], cust[2], cust[3], cust[4], cust[5], cust[6], cust[7]);
    }
}

//!DONE
void read_items(const string& fname){
    string line;
    ifstream f(fname);

    while (getline(f, line)){
        auto itm = split(line, ',');
        items.emplace_back(stoi(itm[0]), itm[1], stod(itm[2]));
    }
}

//!TODO:
void read_orders(const string& fname3){
    string line;
    ifstream f(fname3);

    while (getline(f, line)) {
        auto ordr = split(line, ',');

    }
}

int main(){
    read_items("D:\\UVU\\DavidBennett\\CS2370\\P5\\items.txt");
    read_customers("D:\\UVU\\DavidBennett\\CS2370\\P5\\customers.txt");
    read_orders("D:\\UVU\\DavidBennett\\CS2370\\P5\\orders.txt")

    // for (Item& item: items){
    //     cout << item.get_id() << ',' << item.get_desc() << ',' << item.get_price() << endl;
    // }
    // for (Customer& cust: customers){
    //     cout << cust.print_detail() << endl;
    // };

    //! actual code to use:
    // for (const auto& order: orders){
    //     cout << order.print_order() << endl;
    // };
}

//! everytime theres a new, use a delete or destructor
