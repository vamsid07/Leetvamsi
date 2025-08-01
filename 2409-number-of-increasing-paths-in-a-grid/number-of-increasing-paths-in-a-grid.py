class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        @cache
        def go(i,j) : 
            ans = 0 
            for k in range(4) : 
                ni = i + dr[k] 
                nj = j + dc[k]
                if 0 <= ni < m and 0 <= nj < len(grid[ni]) and grid[ni][nj] > grid[i][j] : 
                    ans += 1 + go(ni,nj)
            return ans
        res = 0 
        MOD = 10**9 + 7
        for i in range(m) : 
            for j in range(len(grid[i])) : 
                res += 1 + go(i,j)
        return res % MOD