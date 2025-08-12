class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i in range(len(nums)):
            max_jump -= 1
            max_jump = max(max_jump, nums[i])
            if max_jump == 0 and i < len(nums) - 1: return False
        
        return True
