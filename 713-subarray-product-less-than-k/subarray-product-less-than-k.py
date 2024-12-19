class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res =   1
        count = 0
        l = 0

        for r, num in enumerate(nums):
            res *= num

            # keep a valid window
            while res >= k and l <= r:
                res = res // nums[l]
                l += 1

            count += r - l + 1

        return count
