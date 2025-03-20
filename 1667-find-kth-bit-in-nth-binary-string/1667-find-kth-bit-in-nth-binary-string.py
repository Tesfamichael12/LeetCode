class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1: return 0
            if n == 2:
                return '011'[k]
            
            t = pow(2, n) - 1
            mid = t // 2
            if k > mid:
                return 1 - int(helper(n, t - k - 1))
            elif k < mid:
                return int(helper(n - 1, k))
            else: 
                return 1
        
        return str(helper(n, k-1))

