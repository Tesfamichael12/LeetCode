class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j-1] + nums[j] > nums[j] + nums[j-1]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]

        nums.reverse()
        return str(int("".join(nums)))