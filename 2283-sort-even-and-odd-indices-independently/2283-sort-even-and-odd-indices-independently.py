class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        even_indexes = [nums[i] for i in range(0, n, 2)] # range(start, end, step)
        odd_indexes = [nums[i] for i in range(1, n, 2)]

        even_indexes.sort()
        odd_indexes.sort(reverse=True)

        even_ptr = odd_ptr = 0
        res = []
        for i in range(n):
            if i % 2 == 0:
                res.append(even_indexes[even_ptr])
                even_ptr += 1
            else:
                res.append(odd_indexes[odd_ptr])
                odd_ptr += 1
        
        return res