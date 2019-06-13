#This takes O(n) time


n = int(input())

def good_fib(n:int)->int:
    if(n<=1):
        return (0, n)
    else:
        (b,a) = good_fib(n-1)
        return (a, a+b)

print(good_fib(n))