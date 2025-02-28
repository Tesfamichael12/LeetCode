class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur, res = 0, 0
        mn, mx = float('inf'), float('-inf')

        for n in nums:
            mn = min(mn, cur)
            mx = max(mx, cur)

            cur += n

            res = max(res, abs(cur - mx), abs(cur - mn))
        
        return res