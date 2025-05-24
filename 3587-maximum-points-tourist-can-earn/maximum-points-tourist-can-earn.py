class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @cache
        def go(cities,days) : 
            # if cities >= n : 
            #     return 0 
            if days >= k : 
                return 0 
            ans = stayScore[days][cities] + go(cities,days+1)
            for j in range(n) :
                ans = max(ans,travelScore[cities][j] + go(j,days+1))
            return ans
        res = float('-inf')
        for i in range(n) : 
            res = max(res,go(i,0))
        return res