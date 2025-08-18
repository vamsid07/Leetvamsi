class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        right = max(quantities)
        left = 1 
        def go(val) : 
            count = 0 
            for i in quantities : 
                count += ceil(i/val)
            if count <= n : 
                return True 
            return False 
        while left <= right :
            mid = ( left + right ) // 2 
            if go(mid) : 
                right = mid - 1 
            else : 
                left = mid + 1 
        return left 