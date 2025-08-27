class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0 
        j = 0
        check = ord('a')
        if len(str1) < len(str2) : 
            return False
        while j < len(str2) : 
            if i >= len(str1) : 
                return False
            if str1[i] == str2[j] : 
                i += 1
                j += 1 
            elif str1[i] != str2[j] : 
                if chr(((ord(str1[i]) - check + 1) % 26) + check) == str2[j] : 
                    j += 1 
                    i += 1 
                else : 
                    i += 1
        return True
            