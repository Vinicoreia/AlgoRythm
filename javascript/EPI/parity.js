'use strict';


const parity = (x) =>{
    let result = 0;
    while(x){
        result ^= 1;
        x &= (x-1); //Drops the lowest set bit of x
    }
    return result;
}

console.log(parity(11))