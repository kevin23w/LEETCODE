class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 , len2 = len(s1) , len(s2)

        if len1 > len2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(len1):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        for i in range(len2 - len1):
            if matches == 26:
                return True
        
            r_idx = ord(s2[i + len1]) - ord("a")
            s2_count[r_idx] += 1

            if s2_count[r_idx] == s1_count[r_idx]:
                matches += 1
            elif s2_count[r_idx] == s1_count[r_idx] + 1:
                matches -= 1
            
            l_idx = ord(s2[i]) - ord("a")
            s2_count[l_idx] -= 1

            if s2_count[l_idx] == s1_count[l_idx]:
                matches += 1
            elif s2_count[l_idx] == s1_count[l_idx] - 1:
                matches -= 1
        return matches == 26                
