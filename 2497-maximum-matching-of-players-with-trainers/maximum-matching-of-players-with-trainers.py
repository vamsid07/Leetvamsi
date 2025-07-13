class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0 
        j = 0 
        n = len(players)
        m = len(trainers)
        count = 0
        while i < n and j < m : 
            if players[i] <= trainers[j] : 
                i += 1 
                j += 1
                count += 1 
            elif players[i] > trainers[j] : 
                j += 1 
        return count