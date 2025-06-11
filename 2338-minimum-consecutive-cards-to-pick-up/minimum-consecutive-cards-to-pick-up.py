class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = defaultdict(int)
        for i in set(cards) : 
            d[i] = float('inf')
        n = len(cards)
        if len(set(cards)) == len(cards) : 
            return -1 
        ans = float('inf')
        for i in range(n): 
            if i-d[cards[i]] +1 > 0 :
                ans = min(ans,i - d[cards[i]] + 1)
            d[cards[i]] = i 
        return ans