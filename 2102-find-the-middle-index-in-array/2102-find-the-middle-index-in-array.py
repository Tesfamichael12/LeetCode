class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        px = list(accumulate(nums))
        sx = list(accumulate((nums[::-1])))
        sx.reverse()

        # print(px)
        # print(sx)

        for i in range(len(px)):
            if px[i] == sx[i]:
                return i

        return -1