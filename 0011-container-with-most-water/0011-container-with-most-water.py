class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) -1
        max_water = 0

        while L < R:
            width = R - L
            current_water = width * min(height[L], height[R])
            max_water = max(max_water , current_water)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max_water