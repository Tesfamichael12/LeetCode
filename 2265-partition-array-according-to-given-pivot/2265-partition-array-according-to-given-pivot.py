class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        first = [num for num in nums if num < pivot]
        mid = [num for num in nums if num == pivot]
        sec = [num for num in nums if num > pivot]

        return first + mid + sec