class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = []
        
        i,j = 0,0
        for row in board:
            for column in row:
                if(column=='.'):
                    pass
                elif(column == 'R'):
                    rook.append(i)
                    rook.append(j)
                j+=1
                    
            i+=1
            j=0
        
        count = 0
        #Moving Left
        for i in range(rook[1], 0, -1):
            if(board[rook[0]][i] == 'p'):
                count+=1
                break
            elif(board[rook[0]][i] == 'B'):
                break
                
                
        #Moving Right
        for i in range(rook[1], 8):
            if(board[rook[0]][i] == 'p'):
                count+=1
                break
            elif(board[rook[0]][i] == 'B'):
                break

        #Moving Up    
        for i in range(rook[0], 0, -1):
            if(board[i][rook[1]] == 'p'):
                count+=1
                break
            elif(board[i][rook[1]] == 'B'):
                break

        #Moving Down
        for i in range(rook[1],8):
            if(board[i][rook[1]] == 'p'):
                count+=1
                break
            elif(board[i][rook[1]] == 'B'):
                break

        return count