class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        def go(freq) : 
            l = 0 
            r = 0 
            temp = 0
            while r < n :
                temp += nums[r]
                if r - l + 1 > freq : 
                    temp -= nums[l]
                    l += 1 
                if r - l + 1 == freq : 
                    if (r-l+1)*nums[r] - temp <= k : 
                        return True
                r += 1 
            return False
        left = 0 
        right = len(nums)
        while left <= right :
            mid = (left + right) // 2 
            if go(mid) : 
                left = mid + 1 
            else : 
                right = mid - 1
        return right