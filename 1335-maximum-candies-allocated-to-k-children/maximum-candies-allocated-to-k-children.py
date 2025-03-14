class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def check(ind) : 
            count = 0
            if ind != 0 : 
                for i in range(len(candies)) : 
                    count += candies[i]//ind
                if count >= k : 
                    return True 
                return False 
            return True
        flag = 0 
        left = 0 
        right = sum(candies)
        while left <= right : 
            mid = ( left + right ) // 2 
            if (check(mid)) : 
                flag = mid 
                left = mid + 1
            else : 
                right = mid - 1 
        return flag