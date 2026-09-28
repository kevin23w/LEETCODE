class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])

            max_len = max(max_len , R - L +1)

        return max_len
