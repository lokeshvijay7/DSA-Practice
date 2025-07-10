class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            width = r - l
            h = min(height[l], height[r])
            area = width * h
            max_water = max(max_water, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
