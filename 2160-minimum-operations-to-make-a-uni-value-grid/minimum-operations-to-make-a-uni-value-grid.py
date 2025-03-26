class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        rem = grid[0][0] % x 
        flag = 1 
        l = []
        for i in range(m) : 
            for j in range(n) : 
                if grid[i][j] % x != rem :
                    flag = 0 
                l.append(grid[i][j])
        if flag == 0 : 
            return -1 
        l.sort() 
        mid1 = l[len(l)//2]
        op1 = 0
        for i in range(m) :
            for j in range(n) :
                temp = abs(grid[i][j] - mid1)
                op1 += temp // x
        return op1

        