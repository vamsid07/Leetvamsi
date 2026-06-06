class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        INF = 10**20
        @cache
        def go(curr,prev) : 
            if curr >= n : 
                return 0
            op1 = go(curr+1,s[curr])
            op2 = -INF
            if s[curr] == '1' : 
                t1 = nums[curr] + go(curr+1,s[curr])
                t2 = -INF
                if prev == '0' : 
                    t2 = nums[curr-1] + go(curr+1,prev)
                op2 = max(t1,t2)
            return max(op1,op2)
        ans = 0 
        if s[0] == '1' : 
            ans = nums[0]
        return ans + go(1,s[0])