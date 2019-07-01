

a = int(input())
# the parity of a binary number is accordingly to the number of 1s int the binary word
# if the number of 1s is odd the parity is 1, otherwise is 0


# There's a lot of solutions to this problem, the first one is O(n) and is just bit shiftting while setting and unsetting the parity bit p using a xor
def parity(x: int) -> int:
    p = 0
    while(x):
        p ^= x&1 # now this shift p everytime x&1 is equal to 1
        print(p)
        x >>= 1
    return p

# There's a rule where if you do a bitwise and between x and x-1 you will erase the lowest set bit
# this way we can reduce the time complexity to O(k) where k is the number of bits setted in the binary numbe
# the worst case is still O(n) though
 
def parity_and(x: int) -> int:
    p =0
    while(x):
        p ^= 1 # this shift p everytime the loop is executed
        x &= (x-1) # unset the lowest set bit
    return result

def fast_parity(x:int) -> int:
    x^= x>>32
    x^= x>>16
    x^= x>>8
    x^= x>>4
    x^= x>>2
    x^= x>>1
    return x & 1

print(fast_parity(a))
