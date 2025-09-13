class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0 
        r = n - 1 
        maxarea = -10000
        while l < r : 
            breadth = r - l
            length = min(height[l],height[r]) 
            area = length*breadth
            maxarea = max(maxarea,area) 
            if height[l] < height[r] : 
                l += 1 
            else : 
                r -= 1 
        return maxarea
            

