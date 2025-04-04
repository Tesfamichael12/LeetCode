class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr):

            j = random.randint(0, len(arr) - 1)
            pivot = arr[j]

            left = []
            right = []
            mid = []
            for i, n in enumerate(arr):
                if n < pivot:
                    left.append(n)
                elif n > pivot:
                    right.append(n)
                else:
                    mid.append(n)

            print(left, right, mid)
            return [left, right, mid]

        def quick_select(arr):
            nonlocal k

            l, r, mid = partition(arr)
            rl, ml = len(r), len(mid)
        
            if rl < k <= rl + ml:
                return mid[0]
            elif rl >= k: 
                return quick_select(r)
            else:
                k -= (rl + ml)# rl + ml is the number of el that are greater than kth el
                return quick_select(l)

        res = quick_select(nums)
        return res
