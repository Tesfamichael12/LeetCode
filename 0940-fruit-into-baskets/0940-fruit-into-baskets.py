class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        maxfruit = 0
        hashmap = defaultdict(int)
        for R in range(len(fruits)):
            hashmap[fruits[R]] += 1

            while len(hashmap) > 2:
                f = fruits[L]
                hashmap[f] -= 1
                if not hashmap[f]: # or hashmap[f] == 0
                    del hashmap[f] # or hashmap.pop(f)
                L += 1
            
            maxfruit = max(maxfruit, R-L+1)
        
        return maxfruit