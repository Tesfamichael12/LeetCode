class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = Counter(costs)
        count = dict(sorted(count.items()))
        ic = 0
        for cost, freq in count.items():
            if coins >= cost * freq: 
                ic += freq
                coins -= cost * freq
            else: 
                ic += coins // cost
                break
        
        return ic
