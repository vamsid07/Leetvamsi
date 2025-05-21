class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        a = 0 
        '''

[[8,5,0,17,15],
 [6,0,15,6,0],
 [7,19,16,8,18],
 [11,3,2,12,13],
 [17,15,15,4,6]]

        '''
        for i in range(n) : 
            for j in range(n) :
                 if i == j : 
                    a += fruits[i][j]
                    fruits[i][j] = 0 
        @cache
        def maxb(i,j,moves) : 
            if (i,j) == (n-1,n-1) : 
                return 0
            if i < 0 or i >= n or j < 0 or j >= n or moves <= 0 : 
                return -float('inf')
            ans = fruits[i][j] + max(maxb(i + 1, j - 1,moves-1),maxb(i + 1, j,moves-1),maxb(i + 1, j + 1,moves-1))
            return ans
        @cache
        def maxc(i,j,moves) : 
            if (i,j) == (n-1,n-1) : 
                return 0
            if i < 0 or i >= n or j < 0 or j >= n or moves <= 0 : 
                return -float('inf')
            ans = fruits[i][j] + max(maxc(i - 1, j + 1,moves-1),maxc(i , j+1,moves-1),maxc(i + 1, j + 1,moves-1))
            return ans
        #print(a,maxb(0,n-1,n-1),maxc(n-1,0,n-1))
        return a + maxb(0,n-1,n-1) + maxc(n-1,0,n-1)