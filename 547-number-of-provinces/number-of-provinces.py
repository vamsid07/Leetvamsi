class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1,n2) : 
            x,y = find(n1),find(n2)
            if x == y : 
                return 0
            if rank[x] < rank[y] : 
                rank[y] += rank[x]
                par[x] = y
            else : 
                rank[x] += rank[y]
                par[y] = x
            return 1
        ans = n 
        for i in range(n) : 
            for j in range(n) : 
                if isConnected[i][j] == 1 : 
                    ans -= union(i,j)
        return ans
            