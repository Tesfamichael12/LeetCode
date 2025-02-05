class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        s = 0
        for num in nums:
            if num % 2 == 0:
                s += num
        
        for i, query in enumerate(queries):
            num = nums[query[1]]
            nums[query[1]] += query[0]
            
            if num % 2 == 0:
                if nums[query[1]] % 2 == 0:
                    s = s - num + nums[query[1]]
                else:
                    s = s - num
            else:
                if nums[query[1]] % 2 == 0:
                    s = s + nums[query[1]]
            
            ans[i] = s
        
        return ans