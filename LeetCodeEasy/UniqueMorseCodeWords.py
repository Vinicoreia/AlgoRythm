# Here we use python set to count the length of unique strings.


class Solution:
    def uniqueMorseRepresentation(self, words):
        a = "abcdefghijklmnopqrstuvwxyz"
        b = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        c = set()

        for word in words:
            newWord = ''
            for letter in word:
                position = a.find(letter)
                newWord += b[position]
            c.add(newWord)
        return len(c)