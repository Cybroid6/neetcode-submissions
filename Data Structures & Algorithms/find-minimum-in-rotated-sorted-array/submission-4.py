class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        low = 0
        high = len(nums) - 1
        while low <= high:
            if nums[low] < nums[high]:
                minimum = min(minimum , nums[low])
                break

            mid = low + (( high - low ) // 2 )
            minimum = min(nums[mid] , minimum)
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return minimum





        
        