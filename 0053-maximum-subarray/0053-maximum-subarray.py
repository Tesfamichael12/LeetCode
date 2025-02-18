class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rn = nums[0]
        mx = max(nums)

        for i in range(1, len(nums)):
            if rn < 0:
                rn = 0
            rn += nums[i]
            # print(rn, nums[i])
            
            mx = max(mx, nums[i], rn)
        
        return mx