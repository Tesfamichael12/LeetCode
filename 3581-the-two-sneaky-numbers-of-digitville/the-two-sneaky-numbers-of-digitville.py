class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashset = set()
        res = []
        for n in nums:
            if n in hashset:
                res.append(n)
            else: hashset.add(n)
        return res
