class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1

        num = str(num)
        res = []
        for c in num:
            res.append(int(c))
        
        return res