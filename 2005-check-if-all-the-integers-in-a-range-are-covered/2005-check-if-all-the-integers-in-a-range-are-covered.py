class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set1 = set()
        for n in range(left, right+1):
            set1.add(n)

        set2 = set()
        for nums in ranges:
            for n in range(nums[0], nums[1]+1):
                set2.add(n)
        print(set2)

        return set1.issubset(set2)