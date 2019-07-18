class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        #Topview is the number of non empty values
        topview = 0
        for x in grid:
            topview += len([i for i in x if i!=0])
        
        #FrontView is equal to the Max value in each position of any array in the grid
        
        frontview = sum(map(max, zip(*grid)))
        # Sideview is equal to the sum of the maximum value of each array in grid
        sideview = sum(map(max, grid))
        return topview + frontview + sideview

        