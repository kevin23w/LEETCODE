class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate ( o , c , curr):
            if o == c == 0:
                res.append(curr)
                return
            if o > 0:
                generate(o-1 , c , curr + "(")
            if o < c:
                generate( o , c-1 , curr + ")")
        generate(n , n , "")
        return res