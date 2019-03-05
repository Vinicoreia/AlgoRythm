#include <bits/stdc++.h>


using namespace std;

string selection_sort( string s){
    int min;
    for( int i =0; i < s.length(); i++){
        min = i;
        for(int j = i+1; j < s.length(); j++){
            if(s[j] < s[min])
                min = j;
            uint32_t aux = s[i];
            s[i] = s[min];
            s[min] = aux;
        }
    }
    return s;
}

int main(){
    string s = "teste";

    string sorted = selection_sort(s);
    cout<< sorted;
    return 0;
}