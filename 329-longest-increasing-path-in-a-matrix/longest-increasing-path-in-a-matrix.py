class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        m = len(matrix)
        n = len(matrix[0])
        @cache
        def go(i,j) : 
            if i < 0 or i >= m or j < 0 or j >= n : 
                return 0
            ans = 0
            for k in range(4) : 
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[i][j]: 
                    ans = max(ans,
                    1 + go(nx,ny))
            return ans
        res = float('-inf')
        for i in range(m) : 
            for j in range(n) : 
                res = max(res,1 + go(i,j))
        return res
