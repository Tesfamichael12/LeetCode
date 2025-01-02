class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sum = 0
        minlen = float('inf')
        l = 0
        for r in range(len(nums)):
            min_sum += nums[r]

            while min_sum >= target:
                minlen = min(minlen, r - l + 1)
                min_sum -= nums[l]
                l += 1
                
        return minlen if minlen != float('inf') else 0