class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        map<long long, long long> count;
        for (auto& c : costs)
            count[c]++;
        
        int ic = 0;
        for (auto& [c, freq] : count)
        {
            // if we multiply c by freq as intigers and their values are 10000 we'll run into overflow so we must make both long long 
            if (coins >= (c * freq))
            {
                ic += freq;
                coins -= (c * freq);
            }
            else{
                ic += coins / c;
                break;
            }
        }
        return ic;
    }
};