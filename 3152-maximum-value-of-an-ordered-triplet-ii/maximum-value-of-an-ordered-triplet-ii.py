class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1,len(nums)) : 
            pref.append(max(pref[-1],nums[i]))
        suff = [nums[-1]] 
        for i in range(len(nums)-2,-1,-1) : 
            suff.append(max(suff[-1],nums[i]))
        suff = suff[::-1]
        maxans = 0
        for j in range(1,len(nums)-1) : 
            maxans = max(maxans,(pref[j-1] - nums[j])*suff[j+1])
        return maxans