class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [0] * len(candies)
        max_val = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_val:
                res[i] = True
            else:
                res[i] = False
        return res