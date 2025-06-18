class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        @cache
        def go(i,j) : 
            if j >= m :
                return 1
            if i >= n : 
                return 0
            op1 = 0
            if s[i] == t[j] :
                op1 = go(i+1,j+1)
            return go(i+1,j) + op1 
        return go(0,0)