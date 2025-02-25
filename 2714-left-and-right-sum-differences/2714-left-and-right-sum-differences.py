class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums = [0] + nums + [0]
        px = list(accumulate(nums))
        nums.reverse()
        sx = list(accumulate(nums))
        sx.reverse()

        print(px)
        print(sx)
        ans = []
        for i in range(1, len(px)-1):
            ans.append(abs(px[i] - sx[i]))
        
        return ans