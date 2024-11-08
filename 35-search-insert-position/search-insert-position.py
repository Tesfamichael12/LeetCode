class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb = bisect.bisect_left(nums, target)
        return lb
        