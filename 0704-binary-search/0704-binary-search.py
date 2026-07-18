class Solution:
    def search(self, arr: list[int], target: int) -> int:
        l , r = 0 , len(arr) -1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] > target:
                r -= 1
            elif arr[m] < target:
                l += 1
            else:
                return m
        return -1