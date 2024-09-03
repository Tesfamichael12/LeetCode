class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        op = cur = 0
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]: cur += 1
            op += cur
        return op