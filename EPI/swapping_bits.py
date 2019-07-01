

# Given a binary number, swap two bits by it's given position:
# Ex: given 100010 1 2
# The result should yields 1000100

def swapping_bits(x: int, i: int, j:int) -> int:
    bitmask = 1<<i | 1 <<j

    if((x>>i) & 1 != (x>>j)&1):
        x ^= bitmask
    return x

print(swapping_bits(10, 2, 1))