class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BSLeft():
            l, r = 0, len(nums) -1 
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                else: 
                    r = mid - 1
            return l

        def BSRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        
        left = BSLeft()
        right = BSRight()

        if left <= right:
            return [left, right]
        return [-1, -1]