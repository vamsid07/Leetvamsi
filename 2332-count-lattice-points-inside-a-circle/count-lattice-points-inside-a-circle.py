class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        vis = set()
        ans = 0 
        for x,y,r in circles : 
            for i in range(x-r,x+r+1) : 
                for j in range(y-r,y+r+1) : 
                    if (x-i)**2 + (y-j)**2 <= r**2 : 
                        if (i,j) not in vis : 
                            ans += 1 
                            vis.add((i,j))
        return ans