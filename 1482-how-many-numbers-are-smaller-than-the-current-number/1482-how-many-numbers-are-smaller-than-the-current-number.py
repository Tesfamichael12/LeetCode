class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sr = sorted(nums)
        res = []
        for n in nums:
            res.append(sr.index(n))

        return res