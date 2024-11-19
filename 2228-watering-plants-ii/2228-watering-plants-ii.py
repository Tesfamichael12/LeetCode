class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refill = 0
        l, r = 0, len(plants) - 1
        A, B = capacityA, capacityB
        while l <= r:
            if l == r:
                max_water = max(A, B)
                if max_water < plants[l]:
                    refill += 1
                break
            if A < plants[l]:
                refill +=1 
                A = capacityA
            A -= plants[l]
            l += 1
            if B < plants[r] and r >= l:
                refill +=1 
                B = capacityB
            B -= plants[r]
            r -= 1
        
        return refill
                

        