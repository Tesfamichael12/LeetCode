class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> balloon = {{'b', 0}, {'a', 0}, {'l', 0}, {'o', 0}, {'n', 0}};
        
        for (char c : text) {
            if (balloon.find(c) != balloon.end()) {
                balloon[c]++;
            }
        }
        
        int valid = balloon['b'];
        valid = min(valid, balloon['a']);
        valid = min(valid, balloon['l'] / 2);
        valid = min(valid, balloon['o'] / 2);
        valid = min(valid, balloon['n']);
        
        return valid;
    }
};