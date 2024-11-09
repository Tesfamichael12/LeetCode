class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1

        L, R = 0, len(nums)-1
        while L <= R:
            mid = (L+R)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                L = mid + 1
            else: 
                R = mid - 1
                