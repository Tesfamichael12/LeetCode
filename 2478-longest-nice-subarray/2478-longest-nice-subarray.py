class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        mask = 0
        l = 0
        max_len = 1
        for r in range(len(nums)):

            # Invalid window; update l
            while mask & nums[r] != 0:
                mask ^= nums[l]
                l += 1
           
            # update the current window
            mask |= nums[r]

            max_len = max(max_len, r - l + 1)
        
        return max_len