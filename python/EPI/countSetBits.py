# Given a number, count the number of bits set to 1 in a integern number


def count_bits(x:int) -> int:
    count = 0
    while(x):
        count += x&1
        x >>= 1
    return count


print(count_bits(10))