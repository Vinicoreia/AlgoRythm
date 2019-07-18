# Input: Given a sequence of n numbers [a1, a2, a3, ...,an]
# Output: A permutation [a1,a2,a3,...,an] such that [a1 <= a2 <= a3,...<=an]

# Insertion sort is a efficient algorithm for sorting a small number of elements.

# Insertion sort is an in place sorting algorithm. This means it does not create 
# another array but scrambles (sort), the numbers within the array itself.

arr = list( map ( int, input().split() ) )

def InsertionSort(arr):

    for j in range(1, len(arr)):
        key=arr[j]
        i = j-1
        while (i >= 0 and arr[i] > key):
            arr[i+1] = arr[i]
            i=i-1

        arr[i+1]=key

InsertionSort(arr)
print(arr)