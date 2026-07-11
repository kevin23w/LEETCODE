class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for characters in words:
                count[ord(characters) - ord('a')] += 1

            anagram[tuple(count)].append(words)
        return list(anagram.values())