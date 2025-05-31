class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 : 
            return 0 
        diff = nums[0] - nums[1]
        ans = 0 
        left = 0
        for right in range(2,n) : 
            if nums[right-1] - nums[right] != diff : 
                left = right - 1 
                diff = nums[right-1] - nums[right]
                continue
            temp = left 
            while right - temp + 1 >= 3 : 
                ans += 1 
                temp += 1 
        return ans