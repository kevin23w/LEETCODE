class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        current = 0
        min_length = float('inf')

        for R in range(len(nums)):
            current += nums[R]
            while current >= target:
                min_length = min(min_length , R - L + 1)
                current -= nums[L]
                L += 1
        return min_length if min_length != float('inf') else 0