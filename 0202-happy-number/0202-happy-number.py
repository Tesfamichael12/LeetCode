class Solution:
    def isHappy(self, n: int) -> bool:
        def digitProductSum(n):
            sum = 0
            while n:
                temp = n % 10
                sum += temp * temp
                n = n // 10
            return sum
        
        slow = fast = n
        while True:
            slow = digitProductSum(slow)
            fast = digitProductSum(fast)
            fast = digitProductSum(fast)
            if slow == fast:
                break
        
        return True if slow == 1 else False
