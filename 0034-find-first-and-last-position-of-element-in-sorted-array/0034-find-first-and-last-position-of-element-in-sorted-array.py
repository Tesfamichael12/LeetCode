class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = bisect.bisect_left(nums, target)
        if lb >= len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = bisect.bisect_right(nums, target)
        return [lb, ub-1]
    