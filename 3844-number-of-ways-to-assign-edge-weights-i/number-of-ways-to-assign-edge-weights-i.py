class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u,v in edges : 
            g[u].append(v)
        q = deque()
        q.append(1) 
        depth = 0
        while q : 
            for i in range(len(q)) :
                n = q.popleft()
                for e in g[n] : 
                    q.append(e)
            depth += 1 
        ed = depth - 1 
        if ed == 1 : 
            return 1
        ans = 2**(ed-1) % (10**9 + 7)
        return ans