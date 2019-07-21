/* Write a program that takes an array of digits representing an integer number and updates the array to represent the integer D+1  */

// Example:
// Input [1,2,9]
// output [1,3,0]

//input [9,9,9]
// output[1,0,0,0]

// The idea here is basically have a carry and add backwards
// if when adding the last index we have a 10 then we set it to 0 and use a carry to add to the next Digit
// if when ended the first Digit is 10 then set it to 1 

const addOne = (A) =>{
    let i = A.length - 1;
    A[i] += 1;

    while(A[i] == 10){
        if(i==0)
            break;
        A[i] = 0;
        i--;
        A[i]+= 1
    }
    if(A[0] == 10){
        A[0] = 1;
        A.push(0);
    }
    return A;
}

console.log(addOne([1,2,9]))
console.log(addOne([1,2,3]))
console.log(addOne([9,9,9,9]))