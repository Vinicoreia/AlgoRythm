#
#       |  1 |  2 |  3 |  4 |
#       | 12 | 13 | 14 |  5 |
#       | 11 | 16 | 15 |  6 |
#       | 10 |  9 |  8 |  7 |
#
# This is the spiral order of an array 4x4 
# Write a function that receives an array NxN and returns the spiral form of this array

from typing import List


A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]



def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # We set the value of visited values to be 0, (a number that is assumed not to be in the matrix)
    shift = ((0,1),(1,0),(0,-1),(-1,0))
    direction, x, y = 0, 0, 0
    spiral_ordering = []

    for _ in range(len(square_matrix)*len(square_matrix)):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x = x + shift[direction][0]
        next_y = y + shift[direction][1]

        if(next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):

            direction = (direction + 1) & 3
            next_x = x + shift[direction][0]
            next_y = y + shift[direction][1]
        
        x,y = next_x, next_y
    return spiral_ordering

print(matrix_in_spiral_order(A))