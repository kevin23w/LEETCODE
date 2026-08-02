class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(st , current_subset ):
            res.append(list(current_subset))
            for i in range(st , len(nums)):
                if i > st and nums[i] == nums[i-1]:
                    continue
                current_subset.append(nums[i])
                bt(i + 1 , current_subset)
                current_subset.pop()
        bt(0 , [])
        return res
