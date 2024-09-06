class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            if n == i + 1: continue # If it's already in the right place pass

            res.extend([i+1, n]) # append the k values 

            
            # arr = arr[:i:-1] + arr[:i]
            # First flip-> bring the largest number to the front
            arr[:i+1] = reversed(arr[:i+1])

            # Second flip-> move the largest number to its final position
            arr[:n] = reversed(arr[:n])
        
        return res

#NOTE
"""
First let's recap on what has been asked:

   - The array arr contains unique integers, and these integers are a permutation of the numbers from 1 to len(arr).
   - The length of the array is <= 100, meaning a brute-force approach is feasible.
   - Any solution that sorts the array using at most 10 * arr.length flips will be considered correct.

The strategy involves moving the largest unsorted number (which is len(arr) at the beginning) to the front of the list by flipping the entire subarray up to that number. Then, we flip the array again to place this number in its correct sorted position.
"""