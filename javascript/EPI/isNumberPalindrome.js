
const isPalindromeNumber = (x) =>{
    const stringNumber = x.toString();
    return stringNumber == stringNumber.split("").reverse().join('');
}

// console.log(isPalindromeNumber(21312));
// console.log(isPalindromeNumber(-21312));
// console.log(isPalindromeNumber(0));
// console.log(isPalindromeNumber(1111));



/*
 With a little bit of mathematical base we can improve this solution to use O(1) space.
 
 To get the Least significant digit we know we only have to do number%10.
 but how can we retrieve the Most Significant digit?

 The number of digits in a decimal number is given by it's log + 1,
 
 numberOfDigits = floor(log(x)) + 1

 now that we know this we can get the most significant digit by doing:

number/(10^(numberOfDigits-1)) 
*/

const isPalindromeN = (n) => {
    if(n<0)
        return false;
    const numberOfDigits = Math.floor(Math.log10(n)) + 1;

    let mostSignificantDigitMask = Math.pow(10, (numberOfDigits -1));
    for(let i =0; i<numberOfDigits/2; i++){
        if(parseInt(n/mostSignificantDigitMask) != n%10) // Compare if the MSD == LSD (Most and least significant digits are equal)
            return false;

        //If they are equal drop the least and most significant digit
        n %= mostSignificantDigitMask // drops the most significant bit;
        n = parseInt(n/10); //drops the least significant digit
        mostSignificantDigitMask = parseInt(mostSignificantDigitMask/100);
    }
    return true;
}

console.log(isPalindromeN(21312));
console.log(isPalindromeN(-21312));
console.log(isPalindromeN(0));
console.log(isPalindromeN(1111));