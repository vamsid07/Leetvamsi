class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        @cache
        def go(i,j) : 
            if i < 0 or j < 0 or i >= m or j >= n : 
                return float('inf')
            if i == m - 1 and j == n - 1 : 
                return 1 + -1*min(0,dungeon[i][j])
            pick = min(go(i+1,j),go(i,j+1)) - dungeon[i][j]
            if pick <= 0 : 
                return 1 
            else : 
                return pick
        return go(0,0)