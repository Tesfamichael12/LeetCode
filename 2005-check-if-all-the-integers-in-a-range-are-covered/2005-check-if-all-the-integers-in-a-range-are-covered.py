class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # since the constraint is small we can brute force it 

        flag = [0] * 51 # given in the constraint, not 50 tho since index start form 0

        for i in range(len(ranges)):
            for j in range(ranges[i][0], (ranges[i][1]) + 1):
                flag[j] = 1 # mark every posible number in the given range start up to end
        
        for k in range(left, right + 1):
            if flag[k] == 0: 
                return False 

        return True 
            
# NOTE     
'''
Alternative method is to sorte ranges first and make an array of size of the first
number which is ranges[0][0] up to the last pair's/range's second number. This will
reduce the usage of the nested loop for the our flag. This method will also reduce memory useage in case if the constraints were higher.  
'''