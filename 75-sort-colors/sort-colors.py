class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l0 = []
        l1 = []
        l2 = []
        for i in nums:
            if i == 0:
                l0.append(i)
            elif i == 1:
                l1.append(i)
            else:
                l2.append(i)
        j = 0 
        for i in range(len(l0)):
            nums[j] = l0[i]
            j += 1
        for i in range(len(l1)):
            nums[j] = l1[i]
            j += 1
        for i in range(len(l2)):
            nums[j] = l2[i]
            j += 1
