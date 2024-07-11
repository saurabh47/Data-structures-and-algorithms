#include <iostream>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
};

class LinkedList
{
public:
    Node *head;
    Node *tail;
    int size;

    LinkedList() : head(NULL), tail(NULL), size(0) {}

    void insertAtEnd(int value)
    {
        if (head == NULL)
        {
            head = new Node();
            head->data = value;
            head->next = NULL;
            tail = head;
            size = 1;
        }
        else
        {
            // creating a New Node wit data
            Node *temp = new Node();
            temp->data = value;
            temp->next = NULL;

            // link the node to linked list
            tail->next = temp;
            // update tail pointer
            tail = tail->next;
            size++;
        }
    }
    void insertAtBeginning(int value)
    {
        if (head == NULL)
        {
            head = new Node();
            head->data = value;
            head->next = NULL;
            size = 1;
        }
        else
        {
            Node *temp = new Node();
            temp->data = value;
            temp->next = head;
            head = temp;
        }
        size++;
    }
    // insert a value after a target in the linkedList
    void insertAfter(int value, int target)
    {
        Node *current = head;
        while (current && (target != current->data))
        {
            current = current->next;
        }
        if (current != NULL)
        {
            Node *temp = new Node();
            temp->data = value;
            temp->next = current->next;
            current->next = temp;
        }
        else
        {
            cout << "target not found, inserting at end" << endl;
            insertAtEnd(value);
        }
    }

    void insertBefore(int value, int target)
    {
        Node *current = head;
        while ((current->next != NULL) && (target != current->next->data))
        {
            current = current->next;
        }
        if (current->next != NULL)
        {
            Node *temp = new Node();
            temp->data = value;
            temp->next = current->next;
            current->next = temp;
        }
        else
        {
            cout << "target not found, inserting at end" << endl;
            insertAtEnd(value);
        }
    }
    // delete target from linked list
    void deleteNode(int target)
    {
        Node *current = head;
        while (current->next && (current->next->data != target))
        {
            current = current->next;
        }
        if (current->next != NULL)
        {
            current->next = current->next->next;
        }
        else
        {
            cout << "target not found" << endl;
        }
    }

    void printList(Node *current = NULL)
    {
        if (current == NULL)
        {
            current = head;
        }
        while (current)
        {
            cout << current->data << "->";
            current = current->next;
        }
        cout << endl;
    }

    Node *reverseList()
    {
        if (head == NULL)
        {
            return head;
        }
        else
        {
            Node *prev = NULL;
            Node *current = head;
            while (current)
            {
                Node *temp = current->next;
                current->next = prev;
                prev = current;
                current = temp;
            }
            return prev;
        }
    }
};

int main()
{
    LinkedList list;
    for (int i = 0; i < 10; i++)
    {
        list.insertAtEnd(i);
    }
    list.printList();
    cout << endl;
    list.insertAtBeginning(100);
    list.printList();
    list.insertAfter(101, 6);
    list.printList();
    list.insertBefore(102, 6);
    list.printList();
    list.head = list.reverseList();
    cout << "reversed list:";
    list.printList();
    list.deleteNode(101);
    list.printList();
    list.deleteNode(101);
    list.printList();
    list.deleteNode(102);
    list.printList();
    return 0;
}
