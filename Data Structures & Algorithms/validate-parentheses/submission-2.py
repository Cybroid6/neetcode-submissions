class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in s:
            if n in '([{':
                stack.append(n)
            elif n == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif n == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif n == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                return False
        return not stack
                