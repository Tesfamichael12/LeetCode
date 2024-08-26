class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxave = ave = float("-inf")
        sum = 0

        l = r = 0
        while r < len(nums):
            while r - l < k:
                sum += nums[r]
                r += 1
            ave = sum / k
            ave = round(ave, 5)
            
            maxave = max(maxave, ave)
            sum -= nums[l]
            l += 1
        return maxave