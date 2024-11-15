class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def cycleSortWithDuplicates():
            i = 0
            while i < n:
                correct_pos = nums[i] - 1
                if nums[i] != nums[correct_pos]:
                    nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
                else:
                    i += 1 
        cycleSortWithDuplicates()
        print(*nums)
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i+1)
        return res