class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        start.sort()
        def go(val):
            st = start[0]
            for i in range(1, n):
                temp = st + val
                if temp <= start[i] + d:
                    st = max(start[i], temp)
                else:
                    return False
            return True
        left = 0
        right = max(start) + d
        while left <= right:
            mid = (left + right) // 2
            if go(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
