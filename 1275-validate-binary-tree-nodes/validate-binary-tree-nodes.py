class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        p = [i for i in range(n)]
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
        indeg = [0]*n
        for i in range(n) :
            if leftChild[i] != -1 : 
                indeg[leftChild[i]] += 1 
                if not union(i,leftChild[i]) : 
                    return False
        for i in range(n) : 
            if rightChild[i] != -1 :
                indeg[rightChild[i]] += 1 
                if not union(i,rightChild[i]) : 
                    return False 
        if indeg.count(0) > 1 : 
            return False
        return True