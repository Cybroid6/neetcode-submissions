class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        a = len(nums)
        output = [1] * a
        for i , n in enumerate(nums):
            for  j , m in enumerate(output[i+1:]):
                output[i] = output[i] * nums[i+1+j]
            for  k , o in enumerate(output[:i]):
                output[i] = output[i] * nums[k]
        return output

            


        