from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longest_streak = 0

        for n in hashset:
            if n - 1 not in hashset:  # find the start of a sequence 
                current_num = n
                current_streak = 1

                while current_num + 1 in hashset:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
