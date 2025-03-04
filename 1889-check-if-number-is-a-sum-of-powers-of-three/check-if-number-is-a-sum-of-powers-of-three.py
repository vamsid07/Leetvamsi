class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0 
        l = []
        while True :
            if pow(3,i) <= n : 
                l.append(pow(3,i))
                i += 1
            else : 
                break 
        m = len(l)
        d = {}
        def go(i,res) : 
            if (i,res) in d : 
                return d[(i,res)]
            if res == n : 
                return True 
            if res > n or i>=m  : 
                return False
            pick = go(i+1,res+l[i])
            notpick = go(i+1,res) 
            d[(i,res)] = pick or notpick
            return d[(i,res)]
        return go(0,0)