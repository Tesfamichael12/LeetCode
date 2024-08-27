class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = l = 0
        
        for r in range(n):
            if nums[r] == 0:
                l = r + 1
            else:
                max1 = max(max1, r - l + 1)
        return max1


