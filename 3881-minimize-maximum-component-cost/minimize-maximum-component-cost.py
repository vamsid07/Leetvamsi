class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0
        edges.sort(key=lambda x: x[2])
        p = list(range(n))
        # r = [0] * n
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            a, b = find(x),find(y)
            if a == b:
                return False
            # if r[a] < r[b]:
            #     a,b = b,a
            p[b] = a
            # if r[a] == r[b]:
            #     r[a] += 1
            return True
        count = n
        for u, v, w in edges:
            if union(u, v):
                count -= 1
                if count == k:
                    return w
        return 0