class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')


        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums)-1

            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]

                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    L += 1
                else:
                    R -= 1
        return closest_sum