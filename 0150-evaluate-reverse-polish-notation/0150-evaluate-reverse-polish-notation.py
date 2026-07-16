class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l = ["+" , "-" , "/" , "*"]
        for i in tokens:
            if i not in l:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(int(b-a))
                elif i == "/":
                    stack.append(int(b/a))
                elif i == "*":
                    stack.append(int(b*a))
        return stack[0]