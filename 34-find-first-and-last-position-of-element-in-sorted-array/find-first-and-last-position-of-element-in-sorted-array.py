class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound():
            l, r = 0, len(nums)-1
            ans = len(nums)
            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= target:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        def upper_bound():
            l, r = 0, len(nums)-1
            ans = len(nums)
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        lb = lower_bound()
        up = upper_bound() - 1
        if lb <= up:
            return [lb, up]
        return [-1, -1]