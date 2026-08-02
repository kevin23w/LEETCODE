class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        visited = [False] * len(nums)

        def backtracking(current_prem):
            if len(current_prem) == len(nums):
                res.append(list(current_prem))
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                visited[i] = True
                current_prem.append(nums[i])

                backtracking(current_prem)

                current_prem.pop()
                visited[i] = False
                
        backtracking([])
        return res
