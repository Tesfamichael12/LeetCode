class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        scores = []
        l, r = 0, nums.count(1)

        for i in range(len(nums)):
            score = l + r
            scores.append(score)

            if nums[i] == 0:
                l += 1
            if nums[i] == 1:
                r -= 1

        scores.append(nums[:len(nums)].count(0) )
        
        max_val = max(scores)
        print(scores)
        res = []
        for i, score in enumerate(scores):
            if score == max_val:
                res.append(i)
        
        return res