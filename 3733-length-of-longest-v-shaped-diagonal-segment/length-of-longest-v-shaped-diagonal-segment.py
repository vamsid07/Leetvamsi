class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def go(i, j, r, c, f, val):
            op1 = 0
            ni, nj = i + r, j + c
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == val:
                nxt = 0 if val == 2 else 2
                op1 = 1 + go(ni, nj, r, c, f, nxt)
            op2 = 0
            if f == 0:
                direc = {
                    (1, 1): (1, -1),
                    (1, -1): (-1, -1),
                    (-1, -1): (-1, 1),
                    (-1, 1): (1, 1)
                }
                if (r, c) in direc:
                    dr, dc = direc[(r, c)]
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == val:
                        nxt = 0 if val == 2 else 2
                        op2 = 1 + go(ni, nj, dr, dc, 1, nxt)
            return max(op1, op2)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans,
                        1 + go(i, j, 1, 1, 0, 2),
                        1 + go(i, j, -1, -1, 0, 2),
                        1 + go(i, j, 1, -1, 0, 2),
                        1 + go(i, j, -1, 1, 0, 2)
                    )
        return ans
