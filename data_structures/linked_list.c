/*
 * File: linked_list.c
 * File Created: Saturday, 3rd September 2022 5:29:34 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Sunday, 4th September 2022 5:54:57 pm
 * Modified By: Mahesh Jamdade
 * -----
 */

#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *link;
};
struct node *start = NULL;

struct node *createNode()
{
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    return newnode;
}

void InsertNodeAtEnd(int x)
{
    struct node *temp = createNode(); /*dynamically created node that is to be added to list*/
    temp->data = x;
    temp->link = NULL;
    /* Now to connect above node to linked list there may be two cases*/
    if (start == NULL)
    {                 /*there may not be any node in the list i.e list is empty*/
        start = temp; /* directly store new nodes address in start/head of list*/
    }
    else
    {                               /*if start points to some other node i.e linked list already contains some nodes*/
        struct node *temp1 = start; /*save the start headress in a temporary variable*/
        while (temp1->link != NULL)
        { /*traverse the list until last node using the temporary variable*/
            temp1 = temp1->link;
        }
        /*when temporary variable points to last node*/
        temp1->link = temp; /*store new nodes address in this last node*/
    }
}

void InsertNodeAtFront(int x)
{
    if (start != NULL)
    {
        struct node *tempAddress = start;    /*store start address in temporary variable*/
        struct node *newnode = createNode(); /*create a node*/
        newnode->data = x;                   /*add data in new node*/
        start = newnode;                     /* store new nodes address in start*/
        newnode->link = tempAddress;         /*add old start address in new nodes link*/
    }
    else
    {
        InsertNodeAtEnd(x);
    }
}

void displayList()
{
    struct node *temp2 = start; /*store starting address in a temporary variable*/
    printf("\nList: ");
    while (temp2 != NULL)
    { /*traverse while end of list using temporary variable*/
        printf("%d ", temp2->data);
        temp2 = temp2->link;
    }
}

/**
 * recursively calls reverse and traverses to the end of the list
 * and once current is null
 * print is executed for all the previous recursion
 * in reverse manner hence we get a reverse linked list
 */
void reverseList(struct node *head)
{
    if (head != NULL)
    {
        reverseList(head->link);
        printf("%d ", head->data);
    }
}

/* Needs a Fix */
void InsertAfter(int index, int x)
{
    int counter = 0;
    struct node *oldaddress, *newnodeAddress = createNode();
    struct node *tempaddress = start;
    newnodeAddress->data = x;
    /*start->3->5->6->7->NULL*/
    if (index == 0)
    {
        InsertNodeAtFront(x);
    }
    else
    {
        while (counter < index)
        {
            oldaddress = tempaddress;
            tempaddress = tempaddress->link;
            counter += 1;
        }
        oldaddress->link = newnodeAddress;
        newnodeAddress->link = tempaddress;
    }
    displayList();
}

/**
 * Deletes the first element of the list 
 * by breaking the link to the first node
 * by simply pointing the start address to the second
 * item in the linked list
 */
void deleteFront()
{
    struct node *startAddress = start;
    if (startAddress != NULL)
    {
        start = startAddress->link;
    }
    else
    {
        printf("\nLIST IS EMPTY NOTHING TO DELETE\n");
    }
}

/**
 * Deletes the last element of the linked list
 * by traversing to the last but one node
 * and point the link of N-1 th node to [NULL] 
 */
void deleteEnd()
{
    struct node *startAddress = start;
    struct node *temp;
    if (start == NULL)
    {
        printf("List is Empty!");
        return;
    }
    while (startAddress->link != NULL)
    {
        temp = startAddress;
        startAddress = startAddress->link;
    }
    temp->link = NULL;
}

int main(/*int argc, char const *argv[]*/)
{
    int n = 100;
    while (n != 0)
    {
        printf("\n1. Insert into List");
        printf("\n2. Insert at front");
        printf("\n3. Insert after node");
        printf("\n4. Delete Front");
        printf("\n5. Delete End");
        printf("\n6. Reverse List");
        printf("\n0. EXIT");
        printf("\nenter your Operation on Linked List:");
        scanf("%d", &n);
        if (n == 0)
            break;
        else if (n == 1)
        {
            int x;
            printf("\nInsert What? \n");
            scanf("%d", &x);
            InsertNodeAtEnd(x);
            displayList();
        }
        else if (n == 2)
        {
            int x;
            printf("\nInsert What? \n");
            scanf("%d", &x);
            InsertNodeAtFront(x);
            displayList();
        }
        else if (n == 3)
        { /*needs a fix*/
            int x, z;
            printf("insert after node position e.g 2\n");
            scanf("%d", &z);
            printf("insert what? ");
            scanf("%d", &x);
            InsertAfter(z, x); /* insert x after zth node*/
        }
        else if (n == 4)
        {
            deleteFront();
            displayList();
        }
        else if (n == 5)
        {
            deleteEnd();
            displayList();
        }
        else if (n == 6)
        {
            printf("ReverseList->");
            reverseList(start);
        }
        else
        {
            printf("Invalid Operation entered\n");
        }
    }
    printf("exited \n");
    return 0;
}	


