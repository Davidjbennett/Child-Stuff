// emp2.cpp: Introduces member functions
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Employee {
    unsigned int emp_id;
    string last_name;
    string first_name;
    string address;
    string city;
    string state;
    string zip;     // String to keep leading zeroes
    double salary;

    // Constructor
    Employee(unsigned int emp_id, const string& last_name, const string& first_name, 
             const string& address, const string& city, const string& state, 
                          const string& zip, double salary) {
        // Note: "this->" not needed
        this->emp_id = emp_id;
        this->last_name = last_name;
        this->first_name = first_name;
        this->address = address;
        this->city = city;
        this->state = state;
        this->zip = zip;
        this->salary = salary;
    }

    string first_last() {                       // Parameter gone
        return first_name + " " + last_name;    // "emp." gone, "this->" not needed
    }
};

int main() {
    vector<Employee> emps;

    // Add some employees
    emps.push_back(Employee(7902,"Smith","Gerald","1234 First Avenue","Chicago","IL","23456",89012.34));
    emps.push_back(Employee(7499,"Allen","Bud","5678 Second Street","Lincoln","NB","45678",78901.23));
    emps.push_back(Employee(7521,"Ward","Robert","90123 Third Blvd","San Luis Obispo","CA","90123",90123.45));

    // Print Employee name and salaries
    for (auto& emp: emps) 
        cout << emp.first_last() << " earns " << emp.salary << endl;

    // Calculate average salary
    double sum = 0.0;
    for (auto& emp: emps)
        sum += emp.salary;
    cout << "Average salary: " << setprecision(2) << fixed << sum/emps.size() << endl;
}

/* Output:
Gerald Smith earns 89012.3
Bud Allen earns 78901.2
Robert Ward earns 90123.4
Average salary: 86012.34
*/