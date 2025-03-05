class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jamp = nums[0]
        for i in range(1, len(nums)):
            max_jamp -= 1
            if max_jamp < 0:
                return False

            max_jamp = max(max_jamp, nums[i])
        
        return True
