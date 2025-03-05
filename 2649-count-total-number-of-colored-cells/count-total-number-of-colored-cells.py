class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1 
        '''
            1 + 4(1) + 4(2) + .... + 4(n-1)
            1 + 4 ( 1 + 2 + 3 +...+(n-1))
            1 + 4(n-1)*(n-2)/2)
        '''

        # for i in range(2,n+1) :
        #     ans += 4*(i-1)
        # return ans

        return 1 + 4*(n)*(n-1)//2