from functools import lru_cache

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totsum = sum(stones)
        n = len(stones)
        d = {}
        def go(i,curr):
            if (i,curr) in d : 
                return d[(i,curr)]
            if i >= n:
                return abs(totsum-2*curr)
            pick = go(i+1,curr+stones[i])
            notpick = go(i+1,curr)
            d[(i,curr)] = min(pick, notpick)
            return d[(i,curr)]
        return go(0,0)
