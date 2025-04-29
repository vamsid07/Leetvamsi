class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxe = max(nums)
        n = len(nums)
        res = 0 
        l = 0 
        r = 0 
        ans = 0
        while r < n : 
            if nums[r] == maxe : 
                res += 1 
            while res >= k : 
                ans += n - r
                if nums[l] == maxe :
                    res -= 1 
                l += 1
            r += 1
        return ans 