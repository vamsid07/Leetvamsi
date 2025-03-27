class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = {}
        maxv = -1
        maxk = -1
        for i in nums : 
            if i in d : 
                d[i] += 1 
            else : 
                d[i] = 1 
            maxv = max(maxv,d[i])
            if d[i] == maxv : 
                maxk = i 
        pref = []
        temp = 0
        for i in nums : 
            if i == maxk : 
                temp += 1 
            pref.append(temp)
        for i in range(len(nums)-1) : 
            left = pref[i]
            right = maxv - pref[i]
            if left*2 > (i + 1) and right*2 > (len(nums) - 1 -i) :
                return i
        return -1
        