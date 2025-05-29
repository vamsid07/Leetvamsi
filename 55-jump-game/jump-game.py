class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        @cache
        def go(index):
            nonlocal seen
            if index >= n - 1:
                return True
            if index in seen:
                return False
            seen.add(index)
            if index + 1 < n :
                for j in range(index + 1,index + nums[index] + 1):
                    if go(j):
                        return True
            return False
        return go(0)
