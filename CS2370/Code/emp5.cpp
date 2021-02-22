// emp5.cpp: Introduces static data and member functions
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Employee {
private:
    inline static int n_objects = 0; // Have to use inline with static
    unsigned int emp_id;             // when initialized in a class
    string last_name;
    string first_name;
    string address;
    string city;
    string state;
    string zip;     // String to keep leading zeroes
    double salary;
public:
    static int get_object_count() {
        return n_objects;
    }

    // Constructor
    Employee(unsigned int id, const string& last, const string& first, 
             const string& addr, const string& cty, const string& st, 
             const string& zp, double sal) {
        emp_id = id;
        last_name = last;
        first_name = first;
        address = addr;
        city = cty;
        state = st;
        zip = zp;
        salary = sal;
        ++n_objects;
    }

    string first_last() const {                 // Note "const"
        return first_name + " " + last_name; 
    }

    // Getters
    unsigned int get_id() const {
        return emp_id;
    }
    string get_last() const {
        return last_name;
    }
    string get_first() const {
        return first_name;
    }
    string get_address() const {
        return address;
    }
    string get_city() const {
        return city;
    }
    string get_state() const {
        return state;
    }
    string get_zip() const {
        return last_name;
    }
    double get_salary() const {
        return salary;
    }

    // Setters (emp_id setter missing because it never changes)
    void set_last(const string& s) {
        last_name = s;
    }
    void set_first(const string& s) {
        first_name = s;
    }
    void set_address(const string& s) {
        address = s;
    }
    void city_city(const string& s) {
        city = s;
    }
    void set_state(const string& s) {
        state = s;
    }
    void set_zip(const string& s) {
        zip = s;
    }
    void set_salary(double amount) {
        salary = amount;
    }
};

double get_avg_salary(const vector<Employee>& emps) {
    double sum = 0.0;
    for (auto& emp: emps)
        sum += emp.get_salary();
    return sum/emps.size();    
}
int main() {
    vector<Employee> emps;
    // How to get n_objects from Employee class
    cout << "Current object count: " << Employee::get_object_count() << "\n\n";

    // Add some employees
    emps.push_back(Employee(7902,"Smith","Gerald","1234 First Avenue","Chicago","IL","23456",89012.34));
    emps.push_back(Employee(7499,"Allen","Bud","5678 Second Street","Lincoln","NB","45678",78901.23));
    emps.push_back(Employee(7521,"Ward","Robert","90123 Third Blvd","San Luis Obispo","CA","90123",90123.45));
    
    cout << "Current object count: " << Employee::get_object_count() << "\n\n";

    // Print Employee name and salaries
    for (auto& emp: emps) 
        cout << emp.first_last() << " earns " << emp.get_salary() << endl;

    // Print average salary
    cout << "Average salary: " << setprecision(2) << fixed << get_avg_salary(emps) << "\n\n";

    // Change Robert's salary
    for (auto& emp: emps) {
        if (emp.get_id() == 7521)
            emp.set_salary(100000.00);
    }

    // Print Employee name and salaries
    for (auto& emp: emps) 
        cout << emp.first_last() << " earns " << emp.get_salary() << endl;

    // Print updated average salary
    cout << "Average salary: " << get_avg_salary(emps) << endl;
}

/* Output:
Current object count: 3

Gerald Smith earns 89012.3
Bud Allen earns 78901.2
Robert Ward earns 90123.4
Average salary: 86012.34

Gerald Smith earns 89012.34
Bud Allen earns 78901.23
Robert Ward earns 100000.00
Average salary: 89304.52
*/
