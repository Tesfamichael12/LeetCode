class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        // since the constraint is small we can brute force it 

        vector<int> flag(51); // given in the constraint, not 50 tho since index start form 0

        for (int i = 0; i < ranges.size(); i++)
        {
            for (int j = ranges[i][0]; j <= ranges[i][1]; j++)
            {
                flag[j] = 1; // mark every posible number in the given range start up to end
            }
        }

        for (int k = left; k <= right; k++){
            if (flag[k] == 0)
               return false;
        }

        return true;
    }
};

// NOTE     
/*
Alternative method is to sorte ranges first and make an array of size of the first
number which is ranges[0][0] up to the last pair's/range's second number. This will
reduce the usage of the nested loop for the our flag. This method will also reduce memory useage in case if the constraints were higher.  
*/