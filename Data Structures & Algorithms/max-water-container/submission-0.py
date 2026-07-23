class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        low = 0
        high = len(heights) - 1 
        while low < high:
            amount_of_water = (high - low) * min(heights[low], heights[high]) 
            if max < amount_of_water:
                max = amount_of_water
                if heights[low] < heights[high]:
                    low +=1
                else:
                    high -= 1
            elif heights[low] < heights[high]:
                low +=1
            else:
                high -= 1
        return max