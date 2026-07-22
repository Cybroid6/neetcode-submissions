import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = []
        for i in s:
            if i.isalnum():
                lis.append(i.lower())
        mid = math.ceil(len(lis)/2)
        for i ,(x , y) in enumerate(zip( lis , lis [::-1] )):
            
            if i == mid :
                return True
            if x != y :
                return False
        return True


