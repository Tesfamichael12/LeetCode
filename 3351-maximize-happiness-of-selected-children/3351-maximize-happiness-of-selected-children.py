class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res, cnt = 0, 0
        i = 0
        while k > 0:
            res += max(happiness[i] - cnt, 0)
            cnt += 1

            i += 1
            k -= 1
        
        return res