class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # greedy, find i with nums[i-1]>nums[i]
        # modify nums[i-1] or nums[i], e.g, [3,4,2,3]
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if count > 1: return False
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i] # modify nums[i-1]
                else:
                    nums[i] = nums[i - 1] # modify nums[i]

        return count <= 1 