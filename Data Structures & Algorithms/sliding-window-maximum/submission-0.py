class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for r in range(len(nums) - k + 1):  # fix: correct stopping point
            maximum = nums[r]               # fix: correct initial value
            for j in nums[r:r + k]:
                maximum = max(maximum, j)
            res.append(maximum)
        return res