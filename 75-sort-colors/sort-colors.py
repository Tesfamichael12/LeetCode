class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
    
        nums.clear()
        nums.extend([0] * count[0])
        nums.extend([1] * count[1])

        nums.extend([2] * count[2])
            
            