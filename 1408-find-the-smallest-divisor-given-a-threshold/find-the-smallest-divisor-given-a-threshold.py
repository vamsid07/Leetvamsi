class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        right = 5*10**6
        left = 1
        def go(val) : 
            temp = 0 
            for i in range(len(nums)) : 
                temp += ceil(nums[i]/val)
            if temp <= threshold : 
                return True 
            return False 
        while left <= right : 
            mid = ( left + right ) // 2 
            if go(mid) : 
                right = mid - 1 
            else : 
                left = mid + 1 
        return left 