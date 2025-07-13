class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p = [i for i in range(26)]
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
        check = ord('a')
        for i in range(len(equations)) : 
            if equations[i][1] == '=' : 
                union(ord(equations[i][0]) - check,ord(equations[i][3]) - check)
        for i in range(len(equations)) : 
            if equations[i][1] == '!' : 
                if find(ord(equations[i][0]) - check) == find(ord(equations[i][3]) - check) :
                    return False
        return True