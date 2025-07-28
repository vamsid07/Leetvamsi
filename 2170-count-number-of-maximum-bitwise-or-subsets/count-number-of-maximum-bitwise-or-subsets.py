class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        bor = 0
        n = len(nums)
        for x in nums:
            bor |= x
        @cache
        def go(i, curr):
            if i == n:
                if curr == bor :
                    return 1 
                return 0
            return go(i+1, curr|nums[i]) + go(i+1, curr)
        return go(0, 0)