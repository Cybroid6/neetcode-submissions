class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        dic = {}

        for s in s1:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1

        dic2 = dic.copy()  

        for r in range(len(s2)):
            start = r  
            if s2[r] in dic:  
                l = r

            while r < len(s2) and r < start + len(s1) and s2[r] in dic:  
                dic2[s2[r]] -= 1  
                r += 1
            if all(v == 0 for v in dic2.values()):
                return True
            else:
                dic2 = dic.copy()  
        return False