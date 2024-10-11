class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        def reverse(left, right): 
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
            
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)