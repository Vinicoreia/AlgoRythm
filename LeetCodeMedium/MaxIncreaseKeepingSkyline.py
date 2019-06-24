class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        TopBottom_maximum = list(map(max, *[i for i in grid]))
        LeftRight_maximum = list(map(max, *zip(*[i for i in grid])))

        i, j, countMax = 0, 0, 0
        for row in grid:
            for column in row:
                if(TopBottom_maximum[j] < LeftRigh_maximum[i]):
                    countMax += TopBottom_maximum[j] - e
                else:
                    countMax += LeftRight_maximum[i] - e
                j+=1
            i+=1
            j=0
        return countMax