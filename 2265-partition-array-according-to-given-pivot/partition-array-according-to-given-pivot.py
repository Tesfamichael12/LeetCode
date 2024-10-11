class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Use a custom key function to sort based on three categories:
        # 1. Elements less than pivot (grouped first)
        # 2. Elements equal to pivot (grouped next)
        # 3. Elements greater than pivot (grouped last)
        nums.sort(key=lambda x: (0 if x < pivot else 1 if x == pivot else 2))
        
        return nums
