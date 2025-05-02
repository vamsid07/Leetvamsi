class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        R = -1
        right = 0 
        dominoes = list(dominoes)
        while right < n :
            if dominoes[right] == 'R' and R == -1 : 
                R = right 
            elif dominoes[right] == 'L' and R == -1 : 
                temp = right - 1 
                while temp >= 0 and dominoes[temp] == '.' : 
                    dominoes[temp] = 'L'
                    temp -= 1 
            elif dominoes[right] == 'L' and R != -1 : 
                R = R + 1 
                lp = right - 1
                while R < lp : 
                    dominoes[R] = 'R'
                    dominoes[lp] = 'L'
                    R += 1
                    lp -= 1
                R = -1
            elif dominoes[right] == 'R' and R != -1 : 
                R = R+1
                while R < right : 
                    dominoes[R] = 'R'
                    R += 1
            right+=1 
        if R != -1 : 
            R += 1
            while R < n : 
                dominoes[R] = 'R'
                R += 1
        return "".join(dominoes)
