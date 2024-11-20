class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length