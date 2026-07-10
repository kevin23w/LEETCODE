class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i , num in enumerate(nums):
            complete = target - num
            if complete in seen:
                return [seen[complete] , i]
            seen[num] = i

