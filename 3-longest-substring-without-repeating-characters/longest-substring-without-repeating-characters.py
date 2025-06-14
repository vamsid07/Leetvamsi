class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        vis = set()
        ans = 0
        n = len(s)
        flag = 0 
        while r < n : 
            if s[r] in vis : 
                ans= max(ans,len(vis))
                while s[r] in vis : 
                    vis.remove(s[l])
                    l += 1
            vis.add(s[r])
            r += 1 
        return max(ans,len(vis))