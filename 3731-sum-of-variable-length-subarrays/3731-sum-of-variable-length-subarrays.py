class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        px = [0] + list(accumulate(nums))
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res += px[i+1] - px[start]

        return res