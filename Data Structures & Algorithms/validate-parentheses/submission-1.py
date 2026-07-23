class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for  i , n in enumerate(s):
            if n in '([{':
                stack.append(n)
            elif n == ')':
                if not stack:
                    return False
                if stack.pop() == '(':
                    continue
                else:
                    return False
            elif n == '}':
                if not stack:
                    return False
                if stack.pop() == '{':
                    continue
                else:
                    return False
            elif n == ']':
                if not stack:
                    return False
                if stack.pop() == '[':
                    continue
                else:
                    return False
            else:
                return False
        
        return not stack
                