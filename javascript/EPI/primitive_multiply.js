// Write a program that multiplies two nonnegative integers.
// The only operators you are allowed to use are
// - assignment
// - bitwise operators 
// equality checks and Boolean combinations.


const multiply = (a, b)=>{
    const sum = (x, y) =>{
        while(y > 0){
            carry = x&y;
            x = x^y;
            y = carry << 1;
        }
        return x;
    }
    result = 0;
    while(a){
        if( a & 1)
            result = sum(result, b);
        a = a >> 1;
        b = b << 1;
    }
    return result;
}

console.log(multiply(3,4))