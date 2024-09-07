class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        const int dx[4] = {0, 1, 0, -1};  // North, East, South, West
        const int dy[4] = {1, 0, -1, 0};
        int x = 0, y = 0, di = 0;
        
        unordered_set<long long> obstacleSet;
        for (const auto& obstacle : obstacles) {
            long long ox = obstacle[0], oy = obstacle[1];
            obstacleSet.insert((ox << 16) | (oy & 0xFFFF));
        }
        
        int maxDistSquared = 0;
        
        for (int cmd : commands) {
            if (cmd == -2) {  // Turn left
                di = (di - 1 + 4) % 4;
            } else if (cmd == -1) {  // Turn right
                di = (di + 1) % 4;
            } else {
                for (int k = 0; k < cmd; ++k) {
                    int nx = x + dx[di], ny = y + dy[di];
                    long long key = ((long long)nx << 16) | (ny & 0xFFFF);
                    if (!obstacleSet.count(key)) {
                        x = nx;
                        y = ny;
                        maxDistSquared = max(maxDistSquared, x*x + y*y);
                    } else {
                        break;
                    }
                }
            }
        }
        
        return maxDistSquared;
    }
};