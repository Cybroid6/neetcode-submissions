class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        result = set()
        
        for i, n in enumerate(s):
            left = i + 1
            right = len(s) - 1
            
            while left < right:
                total = s[i] + s[left] + s[right]
                if total == 0:
                    result.add((s[i], s[left], s[right]))
                    left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(t) for t in result]