class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            tow_sum = nums[l] + nums[r]
            if tow_sum < target:
                l += 1
            elif tow_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return [-1, -1]