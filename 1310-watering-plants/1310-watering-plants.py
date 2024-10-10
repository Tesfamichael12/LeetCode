class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        can = capacity
        
        for i, plant in enumerate(plants):
            if plant > can:
                steps += i*2 
                can = capacity
            steps += 1
            can -= plant
        return steps         
