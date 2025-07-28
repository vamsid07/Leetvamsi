class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        g = defaultdict(list)
        for i in range(len(parents)):
            g[parents[i]].append(i)
        n = len(parents)
        ans = 0
        cnt = 0
        def go(node):
            nonlocal ans, cnt
            if len(g[node]) == 0:
                if n - 1 > ans:
                    ans = n - 1
                    cnt = 1
                elif n - 1 == ans:
                    cnt += 1
                return 1
            temp = 1
            res = 0
            for ch in g[node]:
                sz = go(ch)
                temp *= sz
                res += sz
            if n - res - 1 > 0:
                temp *= (n - res - 1)
            if temp > ans:
                ans = temp
                cnt = 1
            elif temp == ans:
                cnt += 1
            return 1 + res
        go(0)
        return cnt
