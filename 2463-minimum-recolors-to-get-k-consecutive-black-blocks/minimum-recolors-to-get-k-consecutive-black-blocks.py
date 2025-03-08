class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0 
        right = 0 
        n = len(blocks)
        minop = float('inf')
        countw = 0
        countb = 0
        while right < n : 
            if blocks[right] == 'W' : 
                countw += 1 
                countb = 0
            elif blocks[right] == 'B' : 
                countb += 1 
            if countb == k : 
                return 0
            if right - left + 1 == k : 
                minop = min(minop,countw)
                if blocks[left] == 'W' :
                    countw -= 1
                left += 1 
            right += 1 
        return minop