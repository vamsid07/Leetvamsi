from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstpos(l, r):
            pos = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    pos = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return pos

        def lastpos(l, r):
            pos = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    pos = mid
                    l = mid + 1 
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return pos

        return [firstpos(0, len(nums) - 1), lastpos(0, len(nums) - 1)]
