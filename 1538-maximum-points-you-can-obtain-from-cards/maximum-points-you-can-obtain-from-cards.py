class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k > len(cardPoints):
            return -1
        score = 0
        lsum = 0

        lsum = sum(cardPoints[:k])
        score = lsum

        r = len(cardPoints) - 1
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            lsum += cardPoints[r]
            r -= 1

            score = max(score, lsum)
        
        return score