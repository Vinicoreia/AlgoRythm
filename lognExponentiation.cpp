#include <bits/stdc++.h>

using namespace std;

int main(){
    long long int a = 4;
    long long int b = 20;
    /*Computing 4^34 in log(n) time*/
    long long int halvb = floor(b/2);
    long long int result = 0;
    
    
    /* This is supposed to be a log(n) exponentiation for large exponent but pow returns a double so we can't go much further using it.*/
    if(b&1){ /* if b is odd*/
        result = a * pow(pow(a,halvb), 2);
    }else{
        result = pow(pow(a,halvb), 2);
    }
    std::cout<< result<<endl;


    return 0;
}