class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        for i in range(len(grid)) : 
            for j in range(len(grid[i])) : 
                if grid[i][j] == 1 : 
                    row.append(i)
                    col.append(j)
        row.sort()
        col.sort()
        l = row[-1] - row[0] + 1
        b = col[-1] - col[0] + 1 
        return l*b
