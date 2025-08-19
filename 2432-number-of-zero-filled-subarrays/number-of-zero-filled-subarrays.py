class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ct = 0 
        ans = 0 
        for i in nums :
            if i == 0 :
                ct += 1 
            else :
                ans += ct*(ct+1)//2
                ct = 0
        ans += ct*(ct+1)//2
        return ans