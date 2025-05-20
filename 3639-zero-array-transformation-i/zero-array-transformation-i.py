class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        arr = [0 for i in range(n+1)]
        for l,r in queries : 
            arr[l] += 1 
            arr[r+1] -= 1 
        for i in range(1,len(arr)) : 
            arr[i] += arr[i-1]
        for i in range(n) : 
            nums[i] -= arr[i]
            if nums[i] > 0 :
                return False
        return True