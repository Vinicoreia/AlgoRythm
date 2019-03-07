#include <bits/stdc++.h>

using namespace std;

typedef struct nameList {
    string name;
    struct nameList *next;
} nameList;


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




    return 0;
}