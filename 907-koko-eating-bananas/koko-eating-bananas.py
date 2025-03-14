class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def go(ind) :
            count = 0  
            for i in range(len(piles)) : 
                if piles[i] < ind : 
                    count += 1 
                    continue
                else : 
                    count += piles[i] // ind + 1 if piles[i] % ind != 0 else piles[i] // ind
            if count <= h : 
                return True
            return False
        left = 1
        right = max(piles)
        flag = 0 
        while left <= right : 
            mid = (left + right) // 2 
            if ( go(mid)) : 
                flag = mid
                right = mid - 1 
            else : 
                left = mid + 1 
        return flag