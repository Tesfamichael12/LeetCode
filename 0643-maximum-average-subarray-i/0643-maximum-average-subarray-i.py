class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxave = float('-inf')
        sum = 0
        l = 0
        for r in range(len(nums)):

            sum += nums[r]
            if r - l + 1 == k:
                maxave = max(maxave, sum / k)
                sum -= nums[l]
                l += 1
        return maxave