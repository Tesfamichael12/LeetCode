class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> pr_map = {{')', '('}, {']', '['}, {'}', '{'}};
        stack<char> stack;

        for (auto p : s){
            if (pr_map.count(p))
            {
                if (!stack.empty() && stack.top() == pr_map[p])
                    stack.pop();
                else
                    return false;
            }
            else
               stack.push(p);
        }

        return stack.empty();
    }
};