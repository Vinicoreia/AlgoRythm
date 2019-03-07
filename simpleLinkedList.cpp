#include <bits/stdc++.h>

using namespace std;

typedef struct nameList {
    string name;
    struct nameList *next;
} nameList;



void insert(nameList **l, string newName){
    nameList *p; //Creates a new item
    p = (nameList*) malloc(sizeof(nameList)); // Without allocating space and casting to nameList* we would get a Segmentation Fault.
    p->name = newName; //Set its name
    p->next = *l; //Make it point to what was previously the head of the list
    *l=p;   //Assign p as the head of the list now, so this is a insertion at the begining of the list.

}

int main(){

    nameList a;
    nameList b;

    a.name = "Vinicius";
    a.next = &b;
    b.name = "Gabe";
    b.next = NULL;
    cout<< "Adress of A: " << &a <<endl;
    cout<< "Address of B: " << a.next<<endl;
    cout<< "Name in A: " << a.name<<endl;
    cout<< "Name in B through A: " << (*a.next).name<<endl;

    nameList *head = &a;
    insert(&head,"newHead");

    std::cout<<"The Head now is: "<< (head->name);


    return 0;
}