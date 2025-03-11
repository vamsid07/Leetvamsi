class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0 
        right = 0 
        n = len(arr) 
        temp = 0 
        count = 0
        while right < n : 
            temp += arr[right] 
            if right - left + 1 == k : 
                if temp >= k*threshold : 
                    count += 1 
                temp -= arr[left]
                left += 1 
            right += 1 
        return count 