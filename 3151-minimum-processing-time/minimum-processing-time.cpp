class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        sort(processorTime.begin(), processorTime.end());
        sort(tasks.rbegin(), tasks.rend());
        int mintime = 0, k = 0;
        for (int i = 0; i < processorTime.size(); i++)
        {
            int time = processorTime[i] + tasks[k];
            mintime = max(mintime, time);
            k += 4;
        }
        return mintime;
    }
};