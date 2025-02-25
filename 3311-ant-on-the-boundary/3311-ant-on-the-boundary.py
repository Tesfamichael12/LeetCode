class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        px = list(accumulate(nums))
        cnt = px.count(0)
        return cnt