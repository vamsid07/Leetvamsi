class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = "z"*len(s)
        for i in range(len(s)+1) :
            chk1 = s[:i:][::-1] + s[i::] 
            chk2 = s[:len(s)-i:] + s[len(s)-i::][::-1]
            ans = min(ans,chk1,chk2)
        return ans