class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        @cache
        def go(index, op1_count, op2_count):
            if index == n:
                return 0
            ans = nums[index] + go(index+1, op1_count, op2_count)
            if op1_count < op1:
                ans = min(ans, (nums[index]+1)//2 + go(index+1, op1_count+1, op2_count))
            if op2_count < op2 and nums[index] >= k:
                ans = min(ans, nums[index] - k + go(index+1, op1_count, op2_count+1))
            if op1_count < op1 and op2_count < op2 and (nums[index]+1) // 2 >= k:
                ans = min(ans, (nums[index]+1)//2 - k + go(index+1, op1_count+1, op2_count+1))
            if op1_count < op1 and op2_count < op2 and nums[index] >= k:
                ans = min(ans, (nums[index]-k+1)//2 + go(index+1, op1_count+1, op2_count+1))
            return ans
        return go(0, 0, 0)
