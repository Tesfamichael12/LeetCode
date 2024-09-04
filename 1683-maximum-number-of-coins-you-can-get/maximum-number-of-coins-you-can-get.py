class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        steps = len(piles) // 3
        piles.sort(reverse=True)
        sum = 0
        for i in range(1, len(piles) - steps, 2):
            sum += piles[i]
        return sum