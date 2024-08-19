class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2 # to avoid overflow
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                R = mid - 1
            else:
                L = mid + 1
        return -1
        