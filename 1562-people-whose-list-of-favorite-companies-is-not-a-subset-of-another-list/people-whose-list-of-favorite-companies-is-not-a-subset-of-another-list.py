from typing import List
from collections import defaultdict

class Solution:
    def peopleIndexes(self, l: List[List[str]]) -> List[int]:
        n = len(l)
        ans = []
        flag = [0] * n
        for i in range(n):
            d = defaultdict(int)
            for j in range(len(l[i])):
                d[l[i][j]] += 1
            for k in range(n):
                if i == k:
                    continue
                count = 0 
                for m in range(len(l[k])):
                    if d[l[k][m]] > 0:
                        count += 1
                if count == len(l[k]) :
                    flag[k] = 1
        for i in range(n):
            if flag[i] == 0:
                ans.append(i)
        return ans
