class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(maxSum):
            curr = count = 0
            for i in nums:
                count += (i + curr > maxSum)
                curr = curr + i if i + curr <= maxSum else i
            return count + 1 <= k

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2

            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
                
        return l