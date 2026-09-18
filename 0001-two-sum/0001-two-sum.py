class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            val = target - num

            if val in seen:
                return [seen[val],i]
            seen[num] = i
        return []