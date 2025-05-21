class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        prev = -1
        ans = 0
        for i in range(m) : 
            if '1' in bank[i] and prev == -1 :
                prev = bank[i].count('1')
            elif '1' in bank[i] and prev >= 1 :
                ans += prev*bank[i].count('1')
                prev = bank[i].count('1')
        return ans
