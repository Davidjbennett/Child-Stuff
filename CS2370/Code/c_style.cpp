#include <cstring> 
#include <iostream>
using namespace std;

int main() {
    char s1[81];            // Can hold 80 characters + '\0'
    char s2[81];

    // strcpy and strlen
    strcpy(s1, "This, ladies and gentlemen, instead of actual entertainment.");
    cout << s1 << " (" << strlen(s1) << " chars)\n";

    // strncpy
    strncpy(s2, s1, 26);
    s2[26] = '\0';          // After the 'n' in "gentlemen"
    cout << s2 << " (" << strlen(s2) << " chars)\n";

    // strcmp
    cout << strcmp("he", "he") << endl;
    cout << strcmp("he", "help") << endl;
    cout << strcmp("help", "he") << endl;
    cout << 'h' - 'f' << endl;  // These letters are 2 apart
    cout << 'f' - 'h' << endl;  // These letters are -2 apart

    // strcat
    char s3[] = "Now is the time ";
    char s4[] = "for all good carbon-based units ";
    char s5[] = "to run to the aid of their sector";
    strcpy(s1, s3);
    strcat(s1, s4);
    strncat(s1, s5, 6);
    s1[strlen(s3) + strlen(s4) + 6] = '\0';
    cout << s1 << endl;
}

/* Output:
This, ladies and gentlemen, instead of actual entertainment. (60 chars)
This, ladies and gentlemen (26 chars)
0
-1
1
2
-2
Now is the time for all good carbon-based units to run
*/
