# Write a program that takes an integer n and returns an array containing all prime numbers from 1 to n

from typing import List
import math
# Brute Force Solution O(n x sqrt(n))
def BrutePrime( n:int) -> List[int]:
    #for every number we must check to see if it is not multiple of every k from 2 to sqrt(n)
    result = []
    for i in range(2,n+1):
        isPrime = True
        for j in range(2, math.floor(math.sqrt(i)+1)):
            if(i%j == 0):
                isPrime = False
                break
        if(isPrime):
            result.append(i)

    return result
print(BrutePrime(18))

# A better way to do this is, whenever we find a number that is a prime
# we remove all entries who are multiple of that number
# To do this we use a boolean array to encode the candidates
# We use the same approach as before, initially all numbers greater than 2 are primes
# and everytime we find a prime we set all multiple positions to be False
# This is O(n log(log(n))) time complexity 
# (Yes this is correct, there's a good explanation for when an algorithm has this kind 
# of time complexity here https://stackoverflow.com/questions/16472012/what-would-cause-an-algorithm-to-have-olog-log-n-complexity)
def prime_gen(n:int) -> List[int]:
    result = []
    is_prime = [False, False] + [True]*(n-1) # 0 and 1 are by definition false
    
    for i in range(2, n+1):
        if(is_prime[i]):
            # Remove all multiples from now to the end of the array
            result.append(i)
            for j in range(i*2, n+1, i): #Starts at i*2 so we dont exclude our own prime number
                is_prime[j] = False
    return result

print(prime_gen(18))