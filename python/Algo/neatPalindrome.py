# A nice way to check if something is a palindrome in python is:
#
# if you bitwise not a positive integer n you will be left with the -(n+1) number
# since python allow backwards indexing by using negative indices then we can check if something is a palindrome like this





def isPalindrom(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))


print(isPalindrom("teste"))
print(isPalindrom("arara"))
