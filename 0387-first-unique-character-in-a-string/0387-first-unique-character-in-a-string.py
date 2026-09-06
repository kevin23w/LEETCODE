class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            char_counts[index] += 1

        for idxx, char in enumerate(s):
            index = ord(char) - ord('a')
            if char_counts[index] == 1:
                return idxx
        
        return -1
        