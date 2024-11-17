class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # first determine how many piles each person will get 
        piles_per_person = len(piles) // 3
        # sort the piles in decending order 
        piles.sort(reverse=True)
        # Hypotetically we want to give the least piles in the sorted pile for bob
        # [9,8,7,6,5,4,3,2,1] 1, 2, 3 are given for bob
        p = piles_per_person 
        score = piles[1:-p:2] # starting from the second value and increment by 2 until we reach len(piles) - piles_per_person
        return sum(score)