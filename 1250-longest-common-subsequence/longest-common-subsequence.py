class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        @cache
        def go(i,j) : 
            if i >= n or j >= m : 
                return 0 
            if text1[i] == text2[j] : 
                return 1 + go(i+1,j+1)
            return max(go(i+1,j),go(i,j+1))
        return go(0,0)
