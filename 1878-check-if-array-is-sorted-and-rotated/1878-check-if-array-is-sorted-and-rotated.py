class Solution:
    def check(self, nums: List[int]) -> bool:
        index = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                index = i 
                break
        nums = nums[index:] + nums[:index]
        print(nums)
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: 
                return False
        
        return True 