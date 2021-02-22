// list2.cpp: Implements linked list insertion
#include <iostream>
#include <string>
using namespace std;

// Node data structure
struct Node {
    string data;
    Node* next;
    Node(const string& s, Node* nxt) : data(s), next(nxt) {}
};

Node* insert(Node* first, const string& s) {
    if (!first) {   
        // Special case: list is empty (first == nullptr)
        return new Node(s, nullptr);
    }
    else {
        // Find pointer to node before (p) and after (prev) which the new node should go
        Node* p = first;
        Node* prev = nullptr;
        while (p != nullptr && s > p->data) {
            prev = p;
            p = p->next;
        }

        // Create new Node
        Node* new_node = new Node(s, p);
        if (!prev) {
            // Adding new head node
            assert(p == first);
            first = new_node;
        }
        else
            prev->next = new_node;
        return first;
    }
}

int main() {
    Node* head = nullptr;
    for (const string& word: {"flying", "purple", "people", "eater"})
        head = insert(head, word);

    for (Node* p = head; p; p = p->next)    // Condition is p, meaning p != nullptr
        cout << p->data << ' ';
    cout << endl;
}

/* Output:
eater flying people purple 
*/
