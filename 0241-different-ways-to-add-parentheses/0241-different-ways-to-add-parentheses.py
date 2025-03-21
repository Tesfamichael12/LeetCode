class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(expr, memo):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Split the expression into left and right
                    left_results = helper(expr[:i], memo)
                    right_results = helper(expr[i+1:], memo)
                    print(left_results, right_results)
                    # Combine results
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            
            # Base case: if no operator, it's a number
            if not results:
                results.append(int(expr))
            
            memo[expr] = results
            return results
        
        return helper(expression, {})
