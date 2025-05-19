class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float('inf')
        left = 1 
        right = 1
        for i in range(n) : 
            if left == 0 : 
                left = 1 
            if right == 0 : 
                right = 1 
            left *= nums[i]
            right *= nums[n-i-1]
            ans = max(ans,left,right)
        return ans