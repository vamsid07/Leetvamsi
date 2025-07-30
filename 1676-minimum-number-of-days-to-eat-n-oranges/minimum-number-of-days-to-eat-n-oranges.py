class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def go(n) : 
            if n == 1 : 
                return 1
            if n == 0 : 
                return 0 
            op1 = (n%2) + 1 + go((n-(n%2))//2)
            op2 = (n%3) + 1 + go((n-(n%3))//3)
            return min(op1,op2)
        return go(n)