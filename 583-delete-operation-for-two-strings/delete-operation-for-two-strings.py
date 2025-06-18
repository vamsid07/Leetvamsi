class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache
        def go(i,j) : 
            if i >= n : 
                return m - j 
            if j >= m : 
                return n - i
            if word1[i] == word2[j] :
                return go(i+1,j+1)
            return 1 + min(go(i+1,j),go(i,j+1))
        return go(0,0)