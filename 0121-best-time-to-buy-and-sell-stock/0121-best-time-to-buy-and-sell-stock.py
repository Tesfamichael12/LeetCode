class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        curs = prices[0]
        for p in prices:
            curs = min(curs, p)
            maxpro = max(maxpro, p - curs)
        return maxpro