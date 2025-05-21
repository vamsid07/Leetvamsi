class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        vis = set()
        for i in range(m) : 
            for j in range(n) : 
                if matrix[i][j] == 0 and (i,j) not in vis: 
                    vis.add((i,j))
                    rowup = i 
                    rowdown = i 
                    colleft = j
                    colright = j 
                    while rowup >= 0 :
                        if matrix[rowup][j] != 0 : 
                            matrix[rowup][j] = 0
                            vis.add((rowup,j))
                        rowup -=1 
                    while rowdown < m : 
                        if matrix[rowdown][j] != 0 : 
                            matrix[rowdown][j] = 0 
                            vis.add((rowdown,j))
                        rowdown +=1 
                    while colleft >= 0 : 
                        if matrix[i][colleft] != 0 :
                            matrix[i][colleft] = 0 
                            vis.add((i,colleft))
                        colleft -=1 
                    while colright < n : 
                        if matrix[i][colright] != 0 :
                            matrix[i][colright] = 0 
                            vis.add((i,colright))
                        colright +=1 
