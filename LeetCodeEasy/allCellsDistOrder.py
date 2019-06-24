from collections import defaultdict

class Solution:
    def allCellsDistOrder(self, R , C, r0, c0):
        l = defauldict(list)
        target = [r0,c0]
        maxNum = -1
        #O(R*C)
        for i in range(0, R):
            for j in range(0, C):
                ManhattanDistance = abs(r0-i) + abs(c0-j)
                if(ManhattanDistance > maxNum):
                    maxNum = ManhattanDistance
                l[ManhattanDistance].append([i,j])
        result = []
        #Max num é no máximo R*C
        #Aqui é O(maxNum*numero_de_célulasNaMatriz)
        #O((R*C)^2)
        for k in range(0, maxNum+1):
            for i in l[k]:
                result.append(i)
        return result


# One liner mais lento
#       return sorted([[i,j] for i in range(R) for j in range(C)], key = lambda x:abs(x[0]-r0) + abs(x[1]-c0))
