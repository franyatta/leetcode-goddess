class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        mostWater = 0

        while l < r:
            # get the area, length times height
            h = min(height[l], height[r])
            mostWater = max(mostWater, h*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mostWater