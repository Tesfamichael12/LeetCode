class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        # print(nums)

        px = list(accumulate(nums))
        nums.reverse()
        sx = list(accumulate(nums))
        sx.reverse()

        # print(px)
        # print(sx)
        for i in range(len(nums)):
            if px[i] == sx[i]:
                # print(px[i])
                return i + 1
        
        return -1