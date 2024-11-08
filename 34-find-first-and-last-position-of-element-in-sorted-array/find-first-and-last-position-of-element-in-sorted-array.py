class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            l, r = 0, len(nums)-1
            first = -1 
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first
        def last():
            l, r = 0, len(nums)-1
            last = -1 
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return last

        f = first()
        if f == - 1: return [-1, -1]
        la = last()
        return [f, la]