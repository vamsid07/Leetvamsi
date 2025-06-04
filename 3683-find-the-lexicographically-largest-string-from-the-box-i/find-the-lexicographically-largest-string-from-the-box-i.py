class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        ch = ""
        if numFriends == 1 : 
            return word
        for i in range(len(word)) : 
            ch = max(ch,word[i])
        j = 0 
        ans = ""
        while j < len(word) : 
            if word[j] == ch : 
                ans = max(ans,word[j:j+(len(word) - numFriends + 1)])
            j += 1 
        return ans