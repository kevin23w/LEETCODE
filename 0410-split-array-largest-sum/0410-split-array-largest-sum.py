class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # Helper function to check if a max_sum capacity is possible with <= k subarrays
        def can_split(max_sum: int) -> bool:
            subarray_count = 1
            current_sum = 0
            
            for num in nums:
                current_sum += num
                # If current subarray sum exceeds target, start a new subarray
                if current_sum > max_sum:
                    subarray_count += 1
                    current_sum = num  # Reset current sum to the current element
                    
            # True if we can split within the allowed 'k' partitions
            return subarray_count <= k

        # Define the binary search range
        low = max(nums)   # The smallest possible maximum sum (largest single element)
        high = sum(nums)  # The largest possible maximum sum (all elements in one subarray)
        result = high

        # Perform binary search
        while low <= high:
            mid = low + (high - low) // 2
            
            if can_split(mid):
                result = mid      # mid is a valid configuration; record it
                high = mid - 1    # Try to find a smaller maximum sum
            else:
                low = mid + 1     # mid is too small; increase the capacity
                
        return result
