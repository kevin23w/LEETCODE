class Solution:
    def search(self, arr: list[int], target: int) -> int:
        L , R = 0 , len(arr)-1

        while L <= R:
            M = (L + R) // 2
            if arr[M] == target:
                return M
            elif arr[M] < target:
                L = M + 1
            else:
                R = M - 1
        return -1
