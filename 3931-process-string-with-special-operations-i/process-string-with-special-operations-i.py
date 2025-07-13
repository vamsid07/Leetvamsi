class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)
        res = []
        for i in range(n) : 
            if s[i] not in "#%*" : 
                res.append(s[i])
            if len(res) and s[i] == '*' : 
                res.pop() 
            if s[i] == '#' : 
                res = res + res 
            if s[i] == '%' : 
                res = res[::-1]
        return ''.join(res)