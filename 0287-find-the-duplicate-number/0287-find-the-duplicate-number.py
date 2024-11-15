class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0 
        while i < len(nums):
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i +=1 
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
        return len(nums)