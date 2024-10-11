class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i+k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]  