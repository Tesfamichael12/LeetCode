class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = collections.Counter()
        res = 0
        for i in answers:
            if c[i] % (i + 1) == 0:
                res += i + 1
            c[i] += 1
        return res