class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 : 
            return s
        if n % 2 == 0 : 
            temp = sorted(s[:len(s)//2:])
            return ''.join(temp) + ''.join(temp[::-1])
        else : 
            temp = sorted(s[:len(s)//2:])
            return ''.join(temp) + s[len(s)//2] + ''.join(temp[::-1])