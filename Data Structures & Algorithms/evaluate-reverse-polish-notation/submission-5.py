class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = 0
        for i , n in enumerate(tokens):
            if n not in ('+', '-', '*', '/'):
                stack.append(n)
            elif n == '+':
                t = stack.pop()
                s = stack.pop()
                stack.append(str(int(s)+int(t)))
            elif n == '-':
                t = stack.pop()
                s = stack.pop()
                stack.append(str(int(s)-int(t)))
            elif n == '*':
                t = stack.pop()
                s = stack.pop()
                stack.append(str(int(s)*int(t)))
            else:
                t = stack.pop()
                s = stack.pop()
                stack.append(str(int(int(s) / int(t))))
        return int(stack[-1])

        