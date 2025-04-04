class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def KthLargest(arr, k):
            """QuickSelect algorithm using Median of Medians for pivot selection."""
            chunk = 5  # A chunk size of 5 is optimal for median selection

            if len(arr) <= chunk:
                return sorted(arr, reverse=True)[k - 1]  # Directly get the k-th largest

            left, right, mid = partition(arr, chunk)

            right_len, mid_len = len(right), len(mid)

            if right_len < k <= right_len + mid_len:
                return mid[0]  # Found k-th largest element
            elif right_len >= k:
                return KthLargest(right, k)
            else:
                return KthLargest(left, k - (right_len + mid_len))  # Adjust k

        def partition(arr, chunk):
            """Partitions array into three parts: < pivot, == pivot, > pivot"""
            pivot = median(arr, chunk)  # Get pivot using Median of Medians

            left, right, mid = [], [], []
            for n in arr:
                if n < pivot:
                    left.append(n)
                elif n > pivot:
                    right.append(n)
                else:
                    mid.append(n)
            return left, right, mid

        def median(arr, chunk):
            """Finds the median of medians using chunked sorting."""
            medians = []
            for i in range(0, len(arr), chunk):
                group = arr[i:i + chunk]
                group.sort()
                medians.append(group[len(group) // 2])

            # If the number of medians is small, find the median directly
            if len(medians) <= chunk:
                return sorted(medians)[len(medians) // 2]
            else:
                return KthLargest(medians, len(medians) // 2 + 1)  # Select the median from medians

        return KthLargest(nums, k)
