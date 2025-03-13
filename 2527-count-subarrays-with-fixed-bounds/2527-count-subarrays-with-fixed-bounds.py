class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left_bound, last_minK, last_maxK = -1, -1, -1

        res = 0
        for i, val in enumerate(nums):
            if not (minK <= val <= maxK):
                left_bound = i
            
            if val == minK:
                last_minK = i
            if val == maxK:
                last_maxK = i

            if last_minK != -1 and last_maxK != -1:
                res += max(0, min(last_minK, last_maxK) - left_bound)
            
        return res