class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        res = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        
        return right << cnt # right == left      