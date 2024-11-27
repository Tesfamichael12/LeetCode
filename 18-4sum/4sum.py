class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                L, R = j + 1, n - 1
                while L < R:
                    four_sum = nums[i] + nums[j] + nums[L] + nums[R]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                    
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1
                        while L < R and nums[R] == nums[R+1]:
                            R -= 1

                    elif four_sum > target:
                        R -= 1
                    else:
                        L += 1

        return res