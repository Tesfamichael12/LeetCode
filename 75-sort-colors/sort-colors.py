class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using the dutch national flag algo
        l, m, r = 0, 0, len(nums) -1 

        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m, l = m + 1, l + 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -=1
            else:
                m += 1
            
            