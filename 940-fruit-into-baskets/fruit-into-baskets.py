class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        d = {}
        l = 0 
        r = 0 
        n = len(nums)
        count = 0 
        ans = float('-inf')
        while r < n : 
            if nums[r] in d : 
                d[nums[r]] += 1 
            else : 
                d[nums[r]] = 1 
            if len(d) >= 3 : 
                while len(d) >= 3 : 
                    d[nums[l]] -= 1 
                    if d[nums[l]] <= 0 : 
                        del d[nums[l]]
                    l += 1 
            ans = max(ans,r - l + 1)
            r += 1 
        return ans