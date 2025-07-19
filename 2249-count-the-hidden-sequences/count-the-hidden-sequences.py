class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pref = [differences[0]]
        for i in range(1,len(differences)) : 
            pref.append(pref[-1] + differences[i])
        minv = max(lower,lower - min(pref))
        maxv = min(upper,upper - max(pref))
        if minv > maxv : 
            return 0
        return maxv - minv + 1