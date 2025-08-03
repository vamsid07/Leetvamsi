class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 10**9 + 7
        memo = {}
        def go(i,j,tot) :  
            if i == n - 1 and j == m - 1 : 
                if (grid[i][j] + tot) % k == 0 : 
                    return 1 
                else :
                    return 0 
            if i >= n or j >= m : 
                return 0
            if (i,j,tot) in memo : 
                return memo[(i,j,tot)]
            op2 = go(i+1,j,(tot+grid[i][j])%k)
            op1 = go(i,j+1,(tot+grid[i][j])%k)
            memo[(i,j,tot)] = (op1 + op2) % MOD
            return memo[(i,j,tot)]
        return go(0,0,0)