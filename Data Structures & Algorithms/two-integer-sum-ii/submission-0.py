class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        element = 0
        l = []

        for  i , n in enumerate(numbers):
            element = target - numbers[i]
            if element in numbers and numbers.index(element) != i:
                l .append(i+1)
                l.append(numbers.index(element)+1)
                return l  


        