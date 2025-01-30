class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first = num // 3
        print(first)
        if first + first - 1 + first + 1 == num:
            return [first - 1,first, first + 1]
        else:
            return []