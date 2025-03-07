class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp) 
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return res