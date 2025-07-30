class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flag = nums[0]
        count = 0
        if nums[0] == 0 :
            count = 1
        else : 
            count = 0
        for i in range(len(nums)) : 
            if ( nums[i] != flag ) : 
                count += 1 
                flag = not flag 
        return count