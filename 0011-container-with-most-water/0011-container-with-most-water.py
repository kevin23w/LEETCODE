class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1

        while l < r:
            width = r - l
            current_height = min(height[l] , height[r])
            current_area = width * current_height
            max_water = max(max_water , current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
        