class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums)

        for i in range(len(nums) - 2, 0, -1):

            if nums[i] >= j - i - 1:
                j = i + 1
       
        return nums[0] >= j - 1
