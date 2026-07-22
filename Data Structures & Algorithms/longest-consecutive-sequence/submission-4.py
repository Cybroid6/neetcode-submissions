class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = []
        streak = 0


        for value in numSet:
            if (value-1) not in numSet:
                length = 0
                while ( value + length ) in numSet:
                    length +=1
                streak = max(streak,length)
        return streak
            