class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotation_point = k % len(nums)
        k = rotation_point
        if k != 0: 
            nums[:k], nums[k : ] = nums[-k : ], nums[:-k]
        # the rotation_point should be counted for the end of nums
        # Ex. [1, 2, 3, 4, 5, 6, 7]  nums[:k] = [1, 2, 3]
        # But nums[:-k] = [1, 2, 3, 4] which is correct
        # nums[-k:] = [5, 6, 7]