class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, mid, after = [], [], []
        for n in nums:
            if n < pivot: before.append(n)
            elif n == pivot: mid.append(n)
            else: after.append(n)
        print(before, mid, after)
        
        return before + mid + after