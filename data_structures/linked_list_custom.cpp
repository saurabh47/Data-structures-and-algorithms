/*
 * File: linked_list.cpp
 * File Created: Saturday, 3rd September 2022 8:35:13 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Sunday, 4th September 2022 5:54:19 pm
 * Modified By: Mahesh Jamdade
 * -----
 */


// Custom Linked List Implementation in C++

#include <iostream>
using namespace std;

class LinkedList
{
	struct Node
	{
		int data;
		Node *next;

		Node(int x = 0)
		{
			data = x;
			next = NULL;
		}
	};

public:
	Node *head;

	LinkedList()
	{
		head = NULL;
	}

	// push at the end of list
	void push(int x)
	{
		Node *newNode = new Node(x);
		if (head == NULL)
		{
			head = new Node(x);
			return;
		}
		Node *start = head;
		while (start->next != NULL)
		{
			start = start->next;
		}
		start->next = newNode;
	}

	// remove last element of list
	void pop()
	{
		if (head == NULL)
		{
			cout << "list is empty" << endl;
			return;
		}
		if (head->next == NULL)
		{
			head = NULL;
			return;
		}
		Node *start = head;
		Node *temp = head;
		while (start->next != NULL)
		{
			temp = start;
			start = start->next;
		}
		temp->next = NULL;

		if (temp == start)
		{
			head = NULL;
		}
	}

	void display()
	{
		cout << "List:";
		if (head == NULL)
		{
			cout << endl;
			return;
		}
		Node *start = head;
		while (start != NULL)
		{
			cout << start->data << " ";
			start = start->next;
		}
		cout << endl;
	}

	// if insert position is greater than list size, then insert at end
	void insertAt(int index, int item)
	{
		int count = 0;
		if (head == NULL)
		{
			push(item);
			return;
		}
		// insert at the beginning
		if (index == 0)
		{
			Node *newNode = new Node(item);
			newNode->next = head;
			head = newNode;
			return;
		}
		Node *start = head;
		Node *prev = head;

		// insert at mid or end beginning
		while (start->next != NULL && count < index)
		{
			prev = start;
			start = start->next;
			count += 1;
		}
		// if we ve reached the end of the list
		if (count < index)
		{
			push(item);
		}
		else
		{
			Node *newNode = new Node(item);
			newNode->next = start;
			prev->next = newNode;
		}
	}

	void deleteNode(int item)
	{
		Node *prev = head;
		Node *start = head;
		if (start == NULL)
		{
			cout << "List is empty";
			return;
		}
		int count = 0;
		while (item != start->data && start->next != NULL)
		{
			prev = start;
			start = start->next;
			count += 1;
		}
		// if deleting the first element of the list
		if (count == 0)
		{
			head = start->next;
			return;
		}
		if (item == start->data)
		{
			prev->next = start->next;
			cout << "Item found" << endl;
		}
		else
		{
			// reached the end of the list but item not found
			cout << "Item not found" << endl;
		}
	}
};

int main(int argc, char *argv[])
{
	LinkedList list = LinkedList();
	int n;
	do
	{
		cout << "\nChoose an operation to perform" << endl;
		cout << "1.push" << endl;
		cout << "2.pop" << endl;
		cout << "3.insert at" << endl;
		cout << "4.delete" << endl;
		cout << "0.exit" << endl;
		cin >> n;
		if (n == 1)
		{
			cout << "push:";
			int x;
			cin >> x;
			list.push(x);
		}
		else if (n == 2)
		{
			list.pop();
		}
		else if (n == 3)
		{
			int position;
			int item;
			cout << "insert what?";
			cin >> item;
			cout << endl;
			cout << "position:";
			cin >> position;
			list.insertAt(position, item);
		}
		else if (n == 4)
		{
			int item;
			cout << "delete what:";
			cin >> item;
			list.deleteNode(item);
		}
		list.display();
	} while (n != 0);

	return 0;
}

/**
 * Sample Output
 *
	mahesh@Maheshs-MacBook-Air-M1 data_structures % g++ linked_list.cpp -o linked.out
	mahesh@Maheshs-MacBook-Air-M1 data_structures % ./linked.out

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:12
	List:12

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:15
	List:12 15

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:16
	List:12 15 16

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:11
	List:12 15 16 11

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:10
	List:12 15 16 11 10

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	1
	push:9
	List:12 15 16 11 10 9

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	3
	insert what?14

	position:2
	List:12 15 14 16 11 10 9

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	3
	insert what?0

	position:0
	List:0 12 15 14 16 11 10 9

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	3
	insert what?19

	position:54
	List:0 12 15 14 16 11 10 9 19

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	2
	List:0 12 15 14 16 11 10 9

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	2
	List:0 12 15 14 16 11 10

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	2
	List:0 12 15 14 16 11

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	2
	List:0 12 15 14 16

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	4
	delete what:12
	Item found
	List:0 15 14 16

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	4
	delete what:0
	List:15 14 16

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	4
	delete what:16
	Item found
	List:15 14

	Choose an operation to perform
	1.push
	2.pop
	3.insert at
	4.delete
	0.exit
	0
	List:15 14
 */
