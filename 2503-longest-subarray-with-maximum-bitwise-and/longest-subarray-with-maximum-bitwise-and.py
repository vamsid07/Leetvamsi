class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxe = max(nums)
        ans = float('-inf')
        count = 0
        for i in nums : 
            if i == maxe : 
                count += 1 
            else : 
                ans = max(ans,count)
                count = 0
        ans = max(ans,count)
        return ans
            