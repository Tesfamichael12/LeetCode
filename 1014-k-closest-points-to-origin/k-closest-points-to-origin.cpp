class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<pair<int, int>> distances;
        
        for (int i = 0; i < points.size(); ++i) {
            int x = points[i][0];
            int y = points[i][1];
            int d = x * x + y * y;  
            distances.push_back({d, i});
        }
        
        // Sort the distances vector based on the first element (distance)
        sort(distances.begin(), distances.end());

        vector<vector<int>> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(points[distances[i].second]);
        }

        return res;
    }
};
