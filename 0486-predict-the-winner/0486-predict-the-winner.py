class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def pridict(l, r, turn):
            if (l, r) in memo:
                return memo[(l,r)]

            if l == r:
                return nums[l]
            
            if turn:
                left = pridict(l+1, r, not turn) + nums[l]
                right = pridict(l, r-1, not turn) + nums[r]

                memo[(l,r)] = max(left, right)
            else:
                left = pridict(l+1, r, not turn) - nums[l]
                right = pridict(l, r-1, not turn) - nums[r]
            
                memo[(l,r)] = min(left, right)
            
            return memo[(l,r)]
            
        res = pridict(0, len(nums) - 1, True)
        return True if res >= 0 else False