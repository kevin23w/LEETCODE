class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i , num in enumerate(nums):
            ans = target - num
            if ans in D:
                return [D[ans],i]
            D[num] = i