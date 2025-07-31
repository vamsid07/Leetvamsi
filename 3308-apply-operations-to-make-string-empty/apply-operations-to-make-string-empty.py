class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d = defaultdict(int)
        for i in s : 
            d[i] += 1 
        maxv = max(d.values())
        n = len(s)
        vis = set()
        ans = ""
        for i in range(n-1,-1,-1) : 
            if d[s[i]] == maxv and s[i] not in vis : 
                ans += s[i]
                vis.add(s[i])
        return ans[::-1]