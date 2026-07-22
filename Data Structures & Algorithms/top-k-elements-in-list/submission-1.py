class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = c.most_common (k)
        result2 = []
        for i , n in enumerate(result):
            result2.append(result[i][0])
        return result2

        