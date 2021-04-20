#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include "split.h"
#include <iomanip>
using namespace std;

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

    int getCustomerId(){
        return cust_id;
    }

    string print_detail(){
        ostringstream s;
        s << "Customer ID # " << cust_id << ":" << endl;
        s << name << ", ph. " << phone << ", email: " << email << endl;
        s << city << ", " << state << " " << zip << endl;
        return s.str();
    };
};

class Item{
    int item_id;
    string description;
    double price;
public:
    Item(int id, const string& desc, double price) : description(desc){
        this->item_id = id;
        this->price = price;
    }

    int getId(){
        return this->item_id;
    }

    string get_desc(){
        return this->description;
    }

    double get_price(){
        return this->price;
    }
};

class Payment{
    //!Do other classes inherit amount?
protected:
    double amount;
public:
    virtual string print_detail() const = 0;
    virtual ~Payment(){}
    void setAmount(double amount){
        this->amount = amount;
    }
    double getAmount(){
      return this->amount;
    }
};

class Credit : public Payment{
    string card_number;
    string expiration;
public:
    Credit(const string& card_num, const string& exp) : card_number(card_num), expiration(exp){};
    virtual ~Credit(){}
    string print_detail() const override{
        string s = "Paid by Credit card: " + card_number + ", exp. " + expiration;
        return s;
    }
};

class PayPal : public Payment{
    string paypal_id;
public:
    PayPal(const string& id) : paypal_id(id){};
    virtual ~PayPal(){}
    string print_detail() const override{
        string s = "Paid by Paypal ID: " + paypal_id;
        return s;
    }
};

class WireTransfer : public Payment{
    string bank_id;
    string account_id;
public:
    WireTransfer(const string& bnk_id, const string& acc_id) : bank_id(bnk_id), account_id(acc_id){};
    virtual ~WireTransfer(){}
    string print_detail() const override{
        string s = "Paid by Wire transfer from Bank ID " + bank_id + ", Account#" + account_id;
        return s;
    }
};

vector<Item> items;
class LineItem{
    int item_id;
    int quantity;

public:
    LineItem(int id, int qty){
        this->item_id = id;
        this->quantity = qty;
    }

    double sub_total() const{
      double price;
      for(Item x : items){
        if(x.getId() == this->item_id){
          price = x.get_price();
        }
      }
      double total = this->quantity * price;
      return total;
    }

    friend bool operator<(const LineItem& item1, const LineItem& item2) {
        return item1.item_id < item2.item_id;
    }
    int getId(){
        return this->item_id;
    }
    int getQuant(){
        return this->quantity;
    }
};

//!TODO:
vector<Customer> customers;

class Order {
    int order_id;
    string order_date;
    int customer_id;
    vector<LineItem> line_items;
    Payment* payment;

public:
    Order(int id, const string& date, int cust_id, vector<LineItem>& lnItem, Payment* payment) 
            : order_date(date) {
                order_id = id;
                customer_id = cust_id;
                line_items = lnItem;
                this->payment = payment;
                sort(line_items.begin(), line_items.end());
            };

    double total() const{
        double total;
        for(LineItem x : line_items){
          total += x.sub_total();
        }
        return total;
    };

    string print_order() const{
        ostringstream s;
        s << fixed;
        s << setprecision(2);
        s << total();

        string printStr;
        printStr += string(30,'=') + '\n';
        printStr += "Order #" + to_string(order_id) + ", Date: " + order_date + '\n';
        printStr += "Amount: " + s.str() + ", " + payment->print_detail() + "\n\n";
        
        for(int i = 0; i < customers.size();i++){
            if(customers[i].getCustomerId() == this->customer_id){
                printStr += customers[i].print_detail();
            }
        }

        printStr += "\n\nOrder Detail:\n";

        for(LineItem x : line_items){
            printStr += "\t\tItem " + to_string(x.getId()) + ": \"";
            for(Item i :items){
                if(i.getId() == x.getId()){
                    ostringstream a;
                    a << fixed << setprecision(2);
                    a << i.get_price();
                    printStr += i.get_desc() + "\", " +  to_string(x.getQuant()) + " @ " + a.str() + '\n';
                }
            }
        }

        return printStr;
    };

    ~Order() {
    delete payment;
    };
};

void read_customers(const string& fname2){
    string line;
    ifstream f(fname2);

    while (getline(f, line)){
        auto cust = split(line, ',');
        customers.emplace_back(stoi(cust[0]), cust[1], cust[2], cust[3], cust[4], cust[5], cust[6], cust[7]);
    }
}

void read_items(const string& fname){
    string line;
    ifstream f(fname);

    while (getline(f, line)){
        auto itm = split(line, ',');
        items.emplace_back(stoi(itm[0]), itm[1], stod(itm[2]));
    }
}

list<Order> orders;
//!TODO:
void read_orders(const string& fname3){
    string line;
    ifstream f(fname3);

    while (getline(f, line)) {
        auto ordr = split(line, ',');
        vector<LineItem> lnItems;
        for (int x = 3; x < ordr.size(); x++){
            auto itemAndPrice = split(ordr[x],'-');
            int a = stoi(itemAndPrice[0]);
            int b = stoi(itemAndPrice[1]);
            lnItems.emplace_back(LineItem(a,b));
        }

        getline(f,line);
        auto line2 = split(line, ',');

        Payment* paym = nullptr;

        if(stoi(line2[0]) == 1){
            // credit
            // cout << "credit" << endl;
            paym = new Credit(line2[1], line2[2]);
        }else if(stoi(line2[0]) == 2){
            // paypal
            // cout << "paypal" << endl;
            paym = new PayPal(line2[1]);
        }else if(stoi(line2[0]) == 3){
            // wire
            // cout << "wire" << endl;
            paym = new WireTransfer(line2[1], line2[2]);
        }

        orders.emplace_back(stoi(ordr[1]), ordr[2], stoi(ordr[0]), lnItems, paym);
    }
}

int main(){
    read_items("D:\\UVU\\DavidBennett\\CS2370\\P5\\items.txt");
    read_customers("D:\\UVU\\DavidBennett\\CS2370\\P5\\customers.txt");
    read_orders("D:\\UVU\\DavidBennett\\CS2370\\P5\\orders.txt");


    // read_items("items.txt");
    // read_customers("customers.txt");
    // read_orders("orders.txt");

    ofstream ofs("order_report.txt");
    for (const Order& order: orders){
        ofs << order.print_order() << endl;
    }


    // for (Item& item: items){
    //     cout << item.get_id() << ',' << item.get_desc() << ',' << item.get_price() << endl;
    // }
    // for (Customer& cust: customers){
    //     cout << cust.print_detail() << endl;
    // };
}
//! everytime theres a new, use a delete or destructor
