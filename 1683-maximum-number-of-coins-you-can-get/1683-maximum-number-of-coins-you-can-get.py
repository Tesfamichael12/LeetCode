class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        steps = len(piles) // 3
        score = piles[1:-steps:2]
        print(score)
        return sum(score)