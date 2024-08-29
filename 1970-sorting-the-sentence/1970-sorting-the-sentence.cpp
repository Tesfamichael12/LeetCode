class Solution {
public:
    string sortSentence(string s) {
        map<int, string> count;
        stringstream ss(s);
        string word;
        
        while (ss >> word) {
            int pos = word.back() - '0';
            count[pos] = word.substr(0, word.size() - 1);
        }
        
        string out;
        for (const auto& [key, val] : count) {
            if (!out.empty()) out += " ";
            out += val;
        }

        return out;
    }
};
