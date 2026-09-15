class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i , n in enumerate(nums):
            ans = target - n
            if ans in seen:
                return [seen[ans],i]
            seen[n] = i
        return []