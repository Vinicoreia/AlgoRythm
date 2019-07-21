// Given an array of integers reorder its entries such that all even entries appear first


const parityArray = (A) =>{
    const odd = A.filter(x => x%2==1);
    const even = A.filter(x => x%2==0);
    return [...even,...odd];
}

console.log(parityArray([1,2,4,5,6,7,8,9,10]));