class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        listOfWords = text.split()
        firstHit = False
        secondHit = False
        result = []
        for i in range(len(listOfWords)):
            if(firstHit and secondHit):
                result.append(listOfWords[i])
                firstHit = False
                secondHit = False
            if(firstHit):
                if(listOfWords[i] == second):
                    secondHit = True
                else:
                    secondHit = False
                    firstHit = False
            if(listOfWords[i] == first):
                firstHit = True
            
                    
        return result