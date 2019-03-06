#include <bits/stdc++.h>



int main(){
    int a[3][4] = {{1,2,3,4}, 
                   {5,6,3,8}, 
                   {1,2,3,1}};
    int b[4][2] = {{1,2},
                   {3,4},
                   {5,6},
                   {7,8}};

    int Acols = sizeof(a[0]) / sizeof(int);
    int Arows = sizeof(a) / sizeof(a[0]);
    int Bcols = sizeof(b[0])/ sizeof(int);
    int Brows = sizeof(b) / sizeof(b[0]);

    if(Acols !=Brows){
        std::cout<< "Number of Columns in matrix A should be the same as number of rows in  matrix B\n";
        exit(1);
    }

    int c[3][2] = {0};

    for(int i = 0; i< Arows; i++){
        for(int j=0; j < Acols; j++){
            for(int k=0; k < Bcols; k++){
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    int Crows = sizeof(c)/sizeof(c[0]);
    int Ccols = sizeof(c[0])/sizeof(int);

    for(int i =0; i< Crows; i++){
        for(int j=0; j< Ccols; j++){
            std::cout<<c[i][j]<<" ";
        }
        std::cout<<std::endl;

    }
    return 0;
}