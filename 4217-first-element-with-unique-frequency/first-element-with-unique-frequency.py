class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        d = {}
        for i in nums : 
            if i in d :
                d[i] += 1 
            else : 
                d[i] = 1
        l = list(d.values())
        d1 = {}
        for i in l : 
            if i in d1 :
                d1[i] += 1 
            else : 
                d1[i] = 1 
        nl = [] 
        for i in d1 : 
            if d1[i] == 1 : 
                nl.append(i)
        #print(nl)
        if len(nl) == 0 : 
            return -1
        for i in nums : 
            if d[i] == nl[0] : 
                return i
        return -1