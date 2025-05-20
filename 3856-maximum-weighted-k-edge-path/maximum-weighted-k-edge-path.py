class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = defaultdict(list)
        for u,v,w in edges : 
            g[u].append([v,w])
        maxans = -1
        if k == 0 : 
            return 0
        @cache
        def go(i,k,curr) : 
            nonlocal maxans
            if k == 0 : 
                return curr 
            for v,w in g[i] : 
                nw = curr + w 
                if nw < t :
                    ans = go(v,k-1,nw)
                    maxans = max(maxans,ans)
            return -1
        for i in range(n) : 
            temp = go(i,k,0)
        return maxans
            
        
