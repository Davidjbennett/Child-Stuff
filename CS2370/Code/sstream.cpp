// sstream.cpp: Uses string streams
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

struct Employee {
    int emp_id;
    string first_name;
    string last_name;
    Employee(int id, const string& first, const string& last)
        : first_name(first), last_name(last) {
            emp_id = id;
    }
};

int main() {
    vector<Employee> emps;

    // Read employee data into vector
    string line;
    ifstream ifs("emp.dat");
    while (getline(ifs, line)) {
        // Parse line
        istringstream iss(line);
        int id;
        string first, last;
        iss >> id >> first >> last;

        // Add Employee (uses emplace_back so we don't have to create object)
        emps.emplace_back(id, first, last);
    }

    // Display data differently (building output string streams)
    vector<string> emps2;
    for (const Employee& emp: emps) {
        ostringstream oss;
        oss << emp.last_name << ',' << emp.first_name << ',' << emp.emp_id;
        emps2.push_back(oss.str());
    }

    // Display new vector
    for (const string& emp_dat: emps2)
        cout << emp_dat << endl;
}

/* Output:
Scholard,Issie,4678119
Netti,Jed,9609244
Solesbury,Galvan,2771794
Lorenzin,Reynard,469486
Bernardinelli,Sandi,5906217
*/
