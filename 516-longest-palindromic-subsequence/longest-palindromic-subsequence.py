class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(1001)] for j in range(1001)]
        def go(i, j):
            if dp[i][j] : 
                return dp[i][j]
            if i > j:
                return 0
            if i == j:
                return 1
            ans = 0
            if s[i] == s[j]:
                ans = 2 + go(i+1,j-1)
            dp[i][j] = max(ans,go(i+1,j),go(i,j-1))
            return dp[i][j]
        return go(0,n-1)
