class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        for R in range(1, len(nums)):
            if nums[L] == 0 and nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
            if nums[L] != 0:
                L += 1
        