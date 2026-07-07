class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        q = []
        r = list(t)
        u = list(s)
        if len(s) == len(t):
            for i in u:
                for j in r:
                    if j == i:
                        q.append(j)
                        r.remove(j)
                        break
            if len(u) == len(q):
                return True
            else:
                return False





        else:
            return False