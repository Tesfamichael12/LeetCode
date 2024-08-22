class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        i = 0
        while l <= r:
            if nums[l] > nums[r]:
                res[i] = nums[l]
                l += 1
            else:
                res[i] = nums[r]
                r -= 1
            i += 1

        return res[-1::-1]
