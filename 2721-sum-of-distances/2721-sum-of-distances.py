class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_map = defaultdict(list)

        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        res = [0] * len(nums)
        
        for num, indices in index_map.items():
            n = len(indices)
            prefix_sum = 0
            total_sum = sum(indices)  
            
            for i, idx in enumerate(indices):
                left_distance = i * idx - prefix_sum  
                right_distance = (total_sum - prefix_sum - idx) - (n - i - 1) * idx  
                
                res[idx] = left_distance + right_distance
                prefix_sum += idx 
                
        return res
