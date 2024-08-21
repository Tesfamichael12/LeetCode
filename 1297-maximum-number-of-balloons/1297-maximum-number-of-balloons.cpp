class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> count;
        for (char c : text) {
            count[c]++;
        }
        return min({count['b'], count['a'], count['l'] / 2, count['o'] / 2, count['n']});
    }
};