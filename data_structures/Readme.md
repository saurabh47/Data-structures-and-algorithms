### Data Structures

- Linked Lists

*Note: Docs generated via Github copilot*
#### Linked Lists

- [Singly Linked List](singly_linked_list.md)

    Linked lists are a data structure that are linear data structures made up of nodes. Each node contains a value and a pointer to the next node. The first node in the linked list is called the head node. The last node in the linked list is called the tail node.

    Linked lists are very efficient for searching and traversing.

    The time complexity for searching and traversing a linked list is O(n) where n is the number of nodes in the linked list. While, The time complexity for inserting and deleting a node in a linked list is O(1) as compared to O(n) in an array. This is because, in an array, we have to shift the elements to the right or left when we insert or delete an element.But in linked list it is assumed that we have a pointer to the location where we want to insert an element. So, we just have to change the pointer of the previous node to point to the new node and the pointer of the new node to point to the next node. This is why linked lists are very efficient for inserting and deleting elements.

- [Doubly Linked List](doubly_linked_list.md)

    In Doubley Linked List, we have two pointers, one pointing to the next node and the other pointing to the previous node.
    In Singly Linked List, we have only one pointer, pointing to the next node.
    The advantage of using Doubley Linked List is that we can traverse the list in both the directions, i.e. forward and backward. This is not possible in Singly Linked List.
    The disadvantage of using Doubley Linked List is that it takes more memory as compared to Singly Linked List.
