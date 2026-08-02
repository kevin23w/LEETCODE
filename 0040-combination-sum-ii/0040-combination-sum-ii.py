class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start , target , current_comb):
            if target == 0:
                res.append(list(current_comb))
                return
            for i in range(start , len(candidates)):
                if candidates[i] > target : 
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                current_comb.append(candidates[i])
                backtrack(i + 1 , target - candidates[i], current_comb)
                current_comb.pop()
        backtrack(0 , target , [])
        return res