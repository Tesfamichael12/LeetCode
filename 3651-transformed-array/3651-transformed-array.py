class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        for i, num in enumerate(nums):
            if num == 0:
                res[i] = nums[i]
            else:
                indx = (i + num) % n
                res[i] = nums[indx]

        return res