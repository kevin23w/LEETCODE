class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nxt = nums[0]
            nums[0] , nums[nxt] = nums[nxt] , nums[0]
        return nums[0]