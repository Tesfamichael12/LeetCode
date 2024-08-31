class Solution {
public:
    string largestNumber(vector<int>& nums) {
        // Convert all integers to strings
        vector<string> strNums;
        for (int num : nums) {
            strNums.push_back(to_string(num));
        }

        // Define a custom comparator lambda function
        auto compare = [](const string& a, const string& b) {
            return a + b > b + a; // If concatenating a+b is greater than b+a, a should come before b
        };

        // Sort the numbers using the custom comparator
        sort(strNums.begin(), strNums.end(), compare);

        // Concatenate the sorted strings
        string result;
        for (const string& s : strNums) {
            result += s;
        }

        // Handle the edge case where the result might be all zeros
        if (result[0] == '0') {
            return "0";
        }

        return result;
    }
};