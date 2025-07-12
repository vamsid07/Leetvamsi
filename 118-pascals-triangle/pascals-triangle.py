class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 : 
            return [[1]]
        l = [[1],[1,1]]
        for i in range(numRows-2) : 
            temp = [1]
            for j in range(len(l[-1])-1) : 
                temp.append(l[-1][j]+l[-1][j+1])
            temp.append(1)
            l.append(temp)
        return l