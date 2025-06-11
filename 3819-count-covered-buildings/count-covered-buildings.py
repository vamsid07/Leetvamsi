class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        dy = {}
        dx = {}
        for x,y in buildings : 
            if y in dy : 
                dy[y] = (min(dy[y][0],x),max(dy[y][1],x))
            else : 
                dy[y] = (x,x)
            if x in dx : 
                dx[x] = (min(dx[x][0],y),max(dx[x][1],y))
            else : 
                dx[x] = (y,y)
        ans = 0
        for x,y in buildings  :
            if dx[x][0] < y < dx[x][1] and dy[y][0] < x < dy[y][1] : 
                ans += 1
        return ans
        
