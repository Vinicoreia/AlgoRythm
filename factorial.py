a = int(input())
def recursiveFactorial(n):
    if(n<=1):
        return 1
    return n*recursiveFactorial(n-1)

def nonRecursiveFactorial(n):
    count = 1
    for i in range(1, n+1):
        count *= i
    return count
    
print(nonRecursiveFactorial(a))
