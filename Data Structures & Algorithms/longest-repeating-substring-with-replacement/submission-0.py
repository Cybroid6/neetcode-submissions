class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        res = 0
        most_freq = 0
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r] , 0)
            most_freq = max(most_freq , dic[s[r]])

            while (r - l + 1) - most_freq > k:
                dic[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res
