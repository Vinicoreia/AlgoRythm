
const isPalindromeNumber = (x) =>{
    const stringNumber = x.toString();
    return stringNumber == stringNumber.split("").reverse().join('');
}

console.log(isPalindromeNumber(21312))
console.log(isPalindromeNumber(-21312))
console.log(isPalindromeNumber(0))
console.log(isPalindromeNumber(1111))