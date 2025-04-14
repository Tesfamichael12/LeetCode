class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        cnt = 0
        for val in count.values():
            cnt += ( val * (val - 1) // 2 )
        return cnt