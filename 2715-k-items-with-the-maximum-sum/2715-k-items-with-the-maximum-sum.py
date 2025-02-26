class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        
        res = numOnes
        k -= numOnes

        if numZeros > k:
            return res
        
        k -= numZeros
        res -= min(k, numNegOnes)

        return res