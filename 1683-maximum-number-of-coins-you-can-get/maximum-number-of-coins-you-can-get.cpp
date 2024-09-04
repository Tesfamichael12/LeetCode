class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int steps = piles.size() / 3;
        sort(piles.rbegin(), piles.rend());
        int sum = 0;
        for (int i = 1; i < piles.size() - steps; i+=2)
        {
            sum += piles[i];
        }
        return sum;
    }
};