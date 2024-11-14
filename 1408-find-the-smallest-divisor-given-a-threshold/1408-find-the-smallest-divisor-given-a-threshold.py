class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)
        divisor = max_num
        L, R = 1, max_num
        while L <= R:
            mid = (L+R)//2
            total_sum = 0
            for num in nums:
                total_sum += (math.ceil(num/mid))
            if total_sum <= threshold:
                divisor = mid
                R = mid - 1
            else:
                L = mid + 1
        return divisor