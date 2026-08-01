class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        dup = set()
        l = 0
        r = 0
        for i in s:
            while i in dup:
                dup.remove(s[l])
                l += 1
            dup.add(i)
            r += 1
            longest = max(longest, r - l)
        return longest