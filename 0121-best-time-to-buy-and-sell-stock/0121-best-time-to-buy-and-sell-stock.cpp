class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxpro = 0;
        int curs = prices[0];
        for (auto& p : prices)
        {
            curs = min(curs, p);
            maxpro = max(maxpro, p - curs);
        }
        return maxpro;
    }
};