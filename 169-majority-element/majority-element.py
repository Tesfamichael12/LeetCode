class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxval = 1
        maj = nums[0]
        for key, val in count.items():
            if maxval < val:
                maj = key
                maxval = val

        return maj