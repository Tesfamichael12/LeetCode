class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i, box in enumerate(boxes):
            count = 0
            for j in range(i + 1, len(boxes)):
                if boxes[j] == '1':
                    count += (j - i)
            
            res.append(count)

        for i in range(len(boxes) - 1, -1, -1):
            count = 0
            for j in range(i - 1, -1, -1):
                if boxes[j] == '1':
                    count += abs(j - i)
            
            res[i] += count
        
        return res
