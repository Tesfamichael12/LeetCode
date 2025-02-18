class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rn = 0 # running sum
        res = 0
        seen = defaultdict(int)
        seen[0] = 1

        for n in nums:
            rn += n

            # if n - k in seen add the freqency else if n - k not in seen add 0
            res += seen[rn - k]
            seen[rn] += 1 # add the running sum itself for feature use

        return res