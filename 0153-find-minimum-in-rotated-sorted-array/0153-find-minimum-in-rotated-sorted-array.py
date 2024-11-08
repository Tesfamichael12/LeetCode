class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        min_val = nums[0]
        while L <= R:
            mid = (L+R)//2
            # left part is sorted 
            if nums[L] <= nums[mid]:
                min_val = min(min_val, nums[L])
                L = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                R = mid - 1
        
        return min_val