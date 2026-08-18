class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candidate1 ,candidate2 = None , None
        count1 , count2 = 0 , 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        result = []
        target_count = len(nums) // 3

        actual_count1 = nums.count(candidate1)
        actual_count2 = nums.count(candidate2)

        if actual_count1 > target_count:
            result.append(candidate1)
        if candidate2 != candidate1 and actual_count2 > target_count:
            result.append(candidate2)
        return result