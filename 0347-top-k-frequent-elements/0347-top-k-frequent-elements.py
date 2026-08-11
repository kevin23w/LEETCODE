class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1


        bucket = [[] for _ in range(len(nums)+1)]
        for num,freq in count_map.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res