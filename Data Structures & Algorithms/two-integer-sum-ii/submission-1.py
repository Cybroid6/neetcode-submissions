class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if target == sum:
                l.append(left + 1)
                l.append(right + 1)
                return l
            if target < sum:
                right = right - 1
            else:
                left = left + 1

        l.append(left + 1)
        l.append(right + 1)
        return l