class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        prefmax = [nums[0]]
        for i in nums[1::] : 
            if i < prefmax[-1] : 
                prefmax.append(prefmax[-1])
            else :
                prefmax.append(i)
        sufmin = [nums[-1]]
        for i in nums[len(nums)-2::-1] : 
            if i > sufmin[-1] : 
                sufmin.append(sufmin[-1])
            else : 
                sufmin.append(i)
        sufmin = sufmin[::-1]
        for i in range(len(nums)-1) : 
            if prefmax[i] <= sufmin[i+1] : 
                return i + 1
        return 0