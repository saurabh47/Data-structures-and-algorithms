### Data Structures

- Linked Lists

#### Linked Lists

    Linked lists are a data structure that are linear data structures made up of nodes. Each node contains a value and a pointer to the next node. The first node in the linked list is called the head node. The last node in the linked list is called the tail node.

    Linked lists are very efficient for searching and traversing.

    The time complexity for searching and traversing a linked list is O(n) where n is the number of nodes in the linked list. While, The time complexity for inserting and deleting a node in a linked list is O(1) as compared to O(n) in an array. This is because, in an array, we have to shift the elements to the right or left when we insert or delete an element.But in linked list it is assumed that we have a pointer to the location where we want to insert an element. So, we just have to change the pointer of the previous node to point to the new node and the pointer of the new node to point to the next node. This is why linked lists are very efficient for inserting and deleting elements.

    Note: Docs generated via Github copilot