#This takes O(n) time


n = int(input())

def good_fib(n:int)->int:
    if(n<=1):
        return (n,0)
    else:
        (a,b) = good_fib(n-1)
        return (a+b, a)

print(good_fib(n))