class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != 0:
                l += 1
            elif nums[l] == 0 and nums[r]:
                nums[l], nums[r] = nums[r], nums[l] # swap
                l += 1
            r += 1
        