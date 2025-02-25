class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = min(list(accumulate(nums)))
        if res < 0:
            return abs(res) + 1
        else:
            return 1
        # return abs(min(list(accumulate(nums)))) + 1