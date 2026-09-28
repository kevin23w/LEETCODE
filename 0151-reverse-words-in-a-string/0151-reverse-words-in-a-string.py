class Solution:
    def reverseWords(self, s: str) -> str:
        result =  []
        n = len(s)
        i = n - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1
            
            word = ""
            for k in range(j+1 , i+1):
                word += s[k]
            result.append(word)

            i = j

        final_str = ""
        for index in range(len(result)):
            final_str += result[index]
            if index < len(result)-1:
                final_str += ' '
        return final_str
