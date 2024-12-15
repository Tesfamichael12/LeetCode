class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        min_val = min(nums)
        for i in range(min_val, len(nums) + 1):
            if i not in hashset:
                return i
        return 0