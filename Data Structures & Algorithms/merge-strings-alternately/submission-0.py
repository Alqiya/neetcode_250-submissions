class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op=[]
        i,j = 0,0
        while i < len(word1) and j < len(word2):
            op.append(word1[i])
            op.append(word2[j])
            i+=1
            j+=1
        while i <len(word1):
            op.append(word1[i])
            i+=1
        while j < len(word2):
            op.append(word2[j])
            j+=1
        result = "".join(op)
        return result