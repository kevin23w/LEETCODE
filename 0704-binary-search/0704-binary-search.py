class Solution:
    def search(self, arr: list[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            # Bitwise right shift is highly optimized
            mid = (low + high) >> 1
            val = arr[mid]
            
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
