class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxans = -float('inf')
        temp = 0
        for i in range(len(nums)) : 
            temp = max(nums[i],temp+nums[i])
            maxans = max(maxans,temp)
        return maxans