class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_mul = []
        prod = 1
        ans = []
        for i in range(len(nums)) : 
            prod = prod*nums[i] 
            prefix_mul.append(prod)
        print(prefix_mul)
        suffix_mul = []
        prod = 1
        for i in range(len(nums)-1,-1,-1) :
            prod = prod*nums[i]
            suffix_mul.append(prod)
        suffix_mul = suffix_mul[::-1]
        print(suffix_mul)
        for i in range(len(nums)) : 
            if i != 0 and i != len(nums)-1: 
                ans.append(prefix_mul[i-1]*suffix_mul[i+1])
            elif i == 0 : 
                ans.append(suffix_mul[i+1])
            elif i == len(nums) - 1 : 
                ans.append(prefix_mul[i-1])
        #print(prefix_mul,suffix_mul)
        return ans
        