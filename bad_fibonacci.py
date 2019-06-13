#this takes more than O(2^n) time

a = int(input())

def bad_fib(n:int)->int:
    #F0 = 0
    #F1 = 1
    #Fn = F(n-2)+F(n-1)

    if(n<=1):
        return n
    return bad_fib(n-2)+bad_fib(n-1)

print(bad_fib(a))