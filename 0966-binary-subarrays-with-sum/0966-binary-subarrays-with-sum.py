class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prifix = list(accumulate(nums))

        seen = defaultdict(int)
        seen[0] = 1
        res = 0
        for n in prifix:
            res += seen[n - goal]

            seen[n] += 1
        
        return res