class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def go(index, diff): 
            if index >= n - 1: 
                return 0
            pick = float('-inf')
            notpick = go(index + 1, diff)
            if diff == 'P' and nums[index + 1] - nums[index] < 0: 
                pick = 1 + go(index + 1, 'N')
            elif diff == 'N' and nums[index + 1] - nums[index] > 0: 
                pick = 1 + go(index + 1, 'P')
            return max(pick, notpick)
        return 1 + max(go(0, 'P'), go(0, 'N'))
