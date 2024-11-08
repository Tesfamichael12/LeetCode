class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums)-1
        while L <= R:
            mid = (R+L)//2
            if nums[mid] == target:
                return True
            if nums[L] == nums[mid] and nums[R] == nums[mid]:
                L += 1
                R -= 1
                continue

            # left part is sorted
            if nums[L] <= nums[mid]:
                if nums[L] <= target and target <= nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            # right part is sorted
            if nums[mid] <= nums[R]:
                if nums[mid] <= target and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        
        return False