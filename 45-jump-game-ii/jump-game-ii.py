class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def go(index) : 
            if index == n - 1 : 
                return 0 
            if index >= n : 
                return float('inf')
            ans = float('inf')
            for j in range(index+1,index+nums[index]+1) : 
                ans = min(ans,1+go(j))
            return ans
        return go(0)