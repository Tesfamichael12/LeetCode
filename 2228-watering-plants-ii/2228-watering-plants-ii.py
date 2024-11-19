class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refill = 0
        L, R = 0, len(plants) - 1
        alice, bob = capacityA, capacityB
        while L < R:
            if plants[L] > alice:
                alice = capacityA
                refill += 1
            if plants[R] > bob:
                bob = capacityB
                refill += 1
            alice -= plants[L]
            bob -= plants[R]
            L += 1
            R -= 1

            if L == R:
                max_water = max(alice, bob)
                if plants[L] > max_water:
                    refill += 1
        
        return refill
                

        