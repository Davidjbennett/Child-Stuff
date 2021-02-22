#include <ctime>
#include <iostream>
using namespace std;

int main() {
    const time_t tval = time(nullptr);
    auto now = localtime(&tval);
    cout << "Current date and time: ";
    cout << now->tm_mon+1 << '/' << now->tm_mday << '/' << now->tm_year+1900 << ", ";
    cout << now->tm_hour << ':' << now->tm_min << ':' << now->tm_sec << endl;
}

/* Output:
Current date and time: 6/27/120, 19:23:25
*/
