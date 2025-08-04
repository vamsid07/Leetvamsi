class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        l = 0 
        r = 0 
        n = len(fruits)
        ans = float('-inf')
        while r < n : 
            if fruits[r] in d : 
                d[fruits[r]] += 1 
            else : 
                d[fruits[r]] = 1 
            while len(d) >= 3 :
                d[fruits[l]] -= 1 
                if d[fruits[l]] <= 0 : 
                    del d[fruits[l]] 
                l += 1 
            ans = max(ans,r - l + 1)
            r += 1 
        return ans