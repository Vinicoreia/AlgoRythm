// We can solve the classic problem of find all primes from 2 to n using Eratosthenes sieve

const isPrime = (n)=>{

    const sieve = new Array(n).fill(true);
    const primeNumbers = []
    
    for(let i = 2; i<=n; i++){
        if((i*i) > n){
            break
        }
        for(let j = (i*i); j<=n; j+=i){
            if(j%i==0){
                sieve[j] = false;
            }
        }
    }
    for(let i =2; i<sieve.length; i++){
        if(sieve[i])
            primeNumbers.push(i)
    }
    return primeNumbers
}
console.log(isPrime(5))