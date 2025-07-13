class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [i for i in range(n+1)]
        def find(x) : 
            if p[x] != x : 
                p[x] = find(p[x])
            return p[x]
        def union(x,y) : 
            a,b = find(x),find(y)
            if a == b : 
                return False 
            p[b] = a 
            return True 
        for u,v in edges : 
            if union(u,v) : 
                continue
            else : 
                return [u,v]
        return []