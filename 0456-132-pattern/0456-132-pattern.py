class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair of values : Decreasing mono-stack

        mn = nums[0]
        for num in nums:
            
            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and stack[-1][0] > num and num > stack[-1][1]:
                return True

            stack.append([num, mn])
            mn = min(mn, num)
        
        return False