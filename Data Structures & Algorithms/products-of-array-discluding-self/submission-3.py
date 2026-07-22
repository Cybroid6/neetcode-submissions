class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        a = len(nums)
        output = [1] * a
        left = 1
        for i in range(a):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in range(a-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output

            