class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        num = n*(n+1)//2 - sum(nums)
        return num