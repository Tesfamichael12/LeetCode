class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def pridict(l, r):
            if (l, r) in memo:
                return memo[(l,r)]

            if l == r:
                return nums[l]
            
            left = nums[l] - pridict(l + 1, r)
            right = nums[r] - pridict(l, r - 1)

            return max(left, right)
            return memo[(l, r)]
           
        res = pridict(0, len(nums) - 1)
        return True if res >= 0 else False