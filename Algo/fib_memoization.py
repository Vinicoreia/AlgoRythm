import time
table = [-1]*999

def fib(n):
    if(table[n]!=-1):
        return table[n]
    elif(n<=1):
        table[n] = n
        return n
    else:
        f = fib(n-2) + fib(n-1)
        table[n] = f
        return f
begin = time.time()
print(fib(40))
print(time.time()-begin)