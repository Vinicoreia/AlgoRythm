

# Write a function that takes a string
# replace every a in the string for 2 d's
# remove the b's in the string
# example
# input: "abracadabra"
# output: "ddrddcdddddrdd"


# This would be my first solution, this takes O(n) time and O(n) space
def replaceAndRemove1(s:str) -> str:
    result = []
    for i in s:
        if( i == "a"):
            result.append("dd")
        elif(i == "b"):
            pass
        else:
            result.append(i)

    return "".join(result)

print(replaceAndRemove1("abracadabra"))

