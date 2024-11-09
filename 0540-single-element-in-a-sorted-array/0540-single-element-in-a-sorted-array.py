class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]

        L, R = 0, n-1
        while L <= R:
            mid = (L+R) // 2
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid-1] == nums[mid]:
                if mid % 2 != 0:
                    L = mid + 1
                else:
                    R = mid - 1
            elif nums[mid] == nums[mid+1]:
                if mid % 2 != 0:
                    R = mid - 1
                else:
                    L = mid + 1
        