class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0 
        while i < len(nums):
            correct_pos = nums[i] - 1
            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res