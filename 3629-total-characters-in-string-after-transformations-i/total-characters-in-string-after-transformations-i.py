class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d = [0]*26 
        for i in s : 
            d[ord(i) - ord('a')] += 1 
        for i in range(t) :
            nd = [0]*26 
            for i in range(25) : 
                nd[i+1] = d[i]
            # print(d)
            # print(nd)
            nd[0] = d[25]
            nd[1] += nd[0]
            d = nd 
        return sum(d) % (10**9 + 7)