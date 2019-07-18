from typing import List
import collections
import math
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    
    #To check if a sudoku is valid we need to check for duplicates in rows, columns and groups of 3x3 subarrays

    def has_duplicate(A:List[int]) -> bool:
        # receives a block and returns if it contains duplicates or not
        row_column = list(filter(lambda x: x != 0, A))
        return len(row_column) != len(set(row_column))
    
    n = len(partial_assignment)

    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    region_size = int(math.sqrt(n))
    
    return all(not has_duplicate([
        partial_assignment[a][b] 
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
        ]) for I in range(region_size) for J in range(region_size))


# WTF IS THIS
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))

    return max(collections.Counter( k for i, row in enumerate(partial_assignment)
                                    for j, col in enumerate(row) if col != 0
                                    for k in ((i, str(col)), (str(col), j),
                                              (i // region_size, j // region_size, 
                                              str(col)))).values(),
            default=0) <= 1