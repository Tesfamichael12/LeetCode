# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 1, n

        while L <= R:
            mid = L + (R - L) // 2

            if isBadVersion(mid):
                R = mid - 1
            else:
                L = mid + 1

        return L