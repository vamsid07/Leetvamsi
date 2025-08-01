class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        st = intervals[0][0]
        en = intervals[0][1]
        ans = []
        for u,v in intervals[1::] : 
            if u <= en :
                en = max(en,v)
            else :
                ans.append([st,en])
                st = u
                en = v
        ans.append([st,en])
        return ans