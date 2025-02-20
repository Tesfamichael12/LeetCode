class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2])
        mx = trips[-1][2]

        px = [0] * (mx + 2)

        for p, l, r in trips:
            px[l] += p
            px[r] -= p

        px = list(accumulate(px))

        for n in px:
            if n > capacity:
                return False

        return True
        