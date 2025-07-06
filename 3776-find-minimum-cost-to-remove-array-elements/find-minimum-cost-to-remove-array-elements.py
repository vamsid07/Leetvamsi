class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        def go(prev,curr) : 
            if dp[prev][curr] != -1 : 
                return dp[prev][curr]
            if curr >= n : 
                return nums[prev]
            if curr == n - 1 : 
                return max(nums[prev],nums[curr])
            op1 = max(nums[prev],nums[curr]) + go(curr+1,curr+2)
            op2 = max(nums[prev],nums[curr+1]) + go(curr,curr+2)
            op3 = max(nums[curr],nums[curr+1]) + go(prev,curr+2)
            dp[prev][curr] = min(op1,op2,op3)
            return min(op1,op2,op3)
        return go(0,1)