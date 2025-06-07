class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])
        d = n*m
        l = []
        for i in range(m) : 
            l.extend(values[i])
        l.sort(reverse=True)
        ans = 0
        for i in range(len(l)) : 
            ans += d*l[i]
            d -= 1
        return ans