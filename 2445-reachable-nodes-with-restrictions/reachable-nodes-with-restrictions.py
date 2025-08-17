class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(list)
        for u,v in edges : 
            g[u].append(v)
            g[v].append(u)
        q = deque() 
        q.append(0)
        vis = set() 
        vis.add(0)
        count = 0 
        res = set(restricted)
        if 0 in res : 
            return 0
        q = deque() 
        q.append(0)
        vis = set() 
        vis.add(0)
        while q : 
            node = q.popleft() 
            count += 1 
            for nei in g[node] : 
                if nei not in vis and nei not in res: 
                    q.append(nei)
                    vis.add(nei)
        return count