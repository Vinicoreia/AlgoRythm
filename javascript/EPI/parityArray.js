// Given an array of integers reorder its entries such that all even entries appear first

// This solutions uses O(n) space and O(n) time complexity

const parityArray = (A) =>{
    const odd = A.filter(x => x%2==1);
    const even = A.filter(x => x%2==0);
    return [...even,...odd];
}

console.log(parityArray([1,2,4,5,6,7,8,9,10]));


// In the EPI book we can read about an array abstraction using "pointers" so we can partition this array into Even, Unclassified and Odd
// This solution is O(n) in time and O(1) in space complexity
const parityArray1 = (A)=>{
    let next_even=0;
    let next_odd = A.length-1;
    let aux = 0;

    while(next_even < next_odd){
        if(A[next_even]%2 == 0)
            next_even +=1;
        else{ // It's an odd number, we have to swap
            aux = A[next_even];
            A[next_even] = A[next_odd];
            A[next_odd] = aux;
            next_odd -= 1;
        }
    }
    return A;
}
// Since order is not important this solution is also valid;
console.log(parityArray1([1,2,3,4,5,6,7,8,9,10]))