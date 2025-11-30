class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev = []
        d = {}
        for i in range(len(nums)) :
            d[nums[i]] = i 
        minans = float('inf')
        for i in range(len(nums)) : 
            temp = int(str(nums[i])[::-1])
            if temp in d and i < d[temp]:
                minans = min(minans,abs(i-d[temp]))
        return minans if minans != float('inf') else -1