class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub , curSum = nums[0] , 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxsub = max(curSum,maxsub)
        return maxsub
        