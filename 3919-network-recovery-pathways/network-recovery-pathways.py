class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        g = defaultdict(list)
        for u,v,c in edges :
            g[u].append([v,c])
        def check(cost) : 
            n = len(online)
            q = deque()
            q.append((0,0))
            costs = [float('inf')]*n
            costs[0] = 0
            while q : 
                node,c = q.popleft()
                if c > costs[node] : 
                    continue
                for nei,co in g[node] : 
                    if co < cost : 
                        continue 
                    if not online[nei]: 
                        continue
                    nco = co + c 
                    if nco > k : 
                        continue 
                    if nco < costs[nei] :
                        costs[nei] = nco 
                        q.append((nei,nco))
            #print(costs)
            return costs[n-1] <= k 
        right = 0
        left = 0 
        for u,v,c in edges : 
            right = max(right,c)
        while left <= right : 
            mid = (left + right)//2
            if check(mid) : 
                left = mid + 1 
            else : 
                right = mid - 1 
        return right