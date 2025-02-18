class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pr = list(accumulate(nums))
        # print(pr)
        seen = defaultdict(int)
        seen[0] = 1

        res = 0
        for n in pr:
            res += seen[n % k]

            seen[n % k] += 1
        
        return res