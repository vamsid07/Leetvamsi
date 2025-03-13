class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        parr = [0]*(n+1)
        for i in range(len(bookings)) : 
            l = bookings[i][0]
            r = bookings[i][1]
            v = bookings[i][2]
            parr[l-1] += v 
            parr[r] -= v 

        for i in range(1,n+1) : 
            parr[i] = parr[i-1] + parr[i]
        
        return parr[:n]