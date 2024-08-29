class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int f = 0, t = 0;
        for(auto& n : bills)
        {
            if (n == 5){
                f++;
            }
            else if (n == 10){
                if (f > 0){
                    f--;
                    t++;
                }
                else
                    return false;
            }
            else
            {
                if (f > 0 and t > 0){ // both should be at lest one each to make 15$ chenge
                f--, t--;
                }
                else if (f > 2) // 3 * 5 = 15
                {
                    f -= 3;
                }
                else
                    return false;
            }
        }
        return true;
    }
};