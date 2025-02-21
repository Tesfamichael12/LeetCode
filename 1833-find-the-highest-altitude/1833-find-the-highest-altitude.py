class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        px = list(accumulate(gain))
        px = [0] + px

        return max(px)