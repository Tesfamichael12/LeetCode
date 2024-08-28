class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if (arr.size() < 3)
            return false;
        int count = 0;
        for (int i = 1; i < arr.size(); i++)
        {
            if (arr[0] > arr[1] || arr[i - 1] == arr[i])
                return false;
            if (arr[i - 1] > arr[i])
            {
                count++;
                for (int j = i + 1; j < arr.size(); j++)
                {
                    if (arr[j - 1] <= arr[j])
                        return false;
                }
                break;
            }
        }

        return count > 0;
    }
};