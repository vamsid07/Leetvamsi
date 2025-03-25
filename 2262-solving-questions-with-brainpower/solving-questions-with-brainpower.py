class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        d = {}
        def go(i) : 
            if i in d : 
                return d[i]
            if i >= n : 
                return 0
            pick =questions[i][0] + go(i+questions[i][1]+1)
            notpick = go(i+1)
            d[i] = max(pick,notpick)
            return d[i]
        return go(0)