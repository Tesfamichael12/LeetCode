class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        steps = len(piles) // 3
        piles.sort(reverse=True)
        print(piles)
        i = 1
        sum = piles[1]
        while i < len(piles):
            i += 2
            if i < len(piles): sum += piles[i]
            if i+1 == len(piles) - steps: break
        return sum