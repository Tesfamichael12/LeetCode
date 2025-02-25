class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prifix = [0] + list(accumulate(nums))
        seen = set()
        print(prifix)
        for i in range(1, len(prifix)):
            if prifix[i] % k in seen or prifix[i] in seen:
                return True
            
            seen.add(prifix[i-1] % k)

        return False