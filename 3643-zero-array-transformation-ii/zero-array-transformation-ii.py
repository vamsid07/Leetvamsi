class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(queries) 
        m = len(nums)
        left = 0 
        right = n - 1
        flag1 = -1
        if sum(nums) == 0 : 
            return 0
        def check(ind) :
            parr = [0]*(m+1) 
            for i in range(0,ind+1) : 
                l = queries[i][0]
                r = queries[i][1]
                v = queries[i][2]
                parr[l] += v
                parr[r+1] -= v
            
            for i in range(1,m+1) : 
                parr[i] = parr[i-1] + parr[i]
            for i in range(m) : 
                if parr[i] < nums[i] : 
                    return False 
            return True 

        while left <= right : 
            mid = (left + right) // 2 
            if ( check(mid) ) : 
                flag1 = mid
                right = mid - 1
            else : 
                left = mid + 1
        if flag1 == -1 : 
            return -1
        return flag1 + 1