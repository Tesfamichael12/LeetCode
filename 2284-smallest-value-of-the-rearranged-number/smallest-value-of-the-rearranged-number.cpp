class Solution {
public:
    long long smallestNumber(long long num) {
        string s = to_string(abs(num));
        
        if (num < 0) {
            sort(s.begin(), s.end(), greater<char>()); // or sort(s.rbegin(), s.rend());
        } else {
            sort(s.begin(), s.end());
        }
        
        if (num > 0)
        {
            swap(s[0], s[s.find_first_not_of('0')]);
        }
        
        return stoll(s) * (num < 0 ? -1 : 1);
    }
};