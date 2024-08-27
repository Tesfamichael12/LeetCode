class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max1 = count = 0
        
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                max1 = max(max1, count)
                count = 0
        max1 = max(max1, count)

        return max1


