class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 1 2 3 5 1 2   stack = [1, 2, 3, 5]  <= 1 
        MOD = pow(10, 9) + 7

        stack = []
        res = 0
        arr.append(float('-inf')) # handle the remaining el in the stack

        for r in range(len(arr)):
            # mono-increasing to get the min 
            while stack and arr[r] < arr[stack[-1]]:
                i = stack.pop()
                left = i - stack[-1] if stack else i + 1
                right = r - i

                res += (left * right * arr[i]) % MOD
            stack.append(r)
        
        return res % MOD