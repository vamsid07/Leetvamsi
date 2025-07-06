class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def go(i,j) : 
            if i == m - 1 and j == n - 1 : 
                return (i+1)*(j+1)
            if i >= m or i < 0 or j >= n or j < 0 : 
                return float('inf')
            op1 = (i+1)*(j+1) + waitCost[i][j] + min(go(i,j+1),go(i+1,j))
            return op1
        return go(0,0) - waitCost[0][0]
