class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            ans[i] = nums[n]
        
        return ans