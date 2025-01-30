class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(n):
            reversed = 0
            while n:
                reversed = reversed * 10 + n % 10
                n //= 10
            
            return reversed

        count = set()
        for num in nums:
            if num not in count:
                count.add(num)
            if rev(num) not in count:
                count.add(rev(num))
            
        return len(count)