class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = sum(nums[:3])
        for i in range(len(nums)):
            L, R = i+1, len(nums)-1

            while L < R:
                closest = nums[i] + nums[L] + nums[R]
                if abs(target - closest) < abs(target - res):
                    res = closest
                
                if closest > target:
                    R -= 1
                elif closest < target:
                    L += 1
                else:
                    return closest
        
        return res