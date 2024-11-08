class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        min_val = nums[0]
        while L <= R:
            mid = (R + L) // 2

            if nums[L] == nums[mid] and nums[R] == nums[mid]:
                min_val = min(min_val, nums[mid]) # or nums[L] or nums[R]
                L += 1
                R -= 1
                continue

            # left half is sorted 
            if nums[L] <= nums[mid]:
                min_val = min(min_val, nums[L])
                L = mid + 1
            else: # right half is sorted 
                min_val = min(min_val, nums[mid])
                R = mid - 1
            
        return min_val