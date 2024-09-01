class Solution {
public:
    int countUnguarded(int r, int c, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<char>> grid(r, vector<char>(c, '0'));
        
        // Mark the positions of guards and walls on the grid
        for (const auto& guard : guards) {
            grid[guard[0]][guard[1]] = 'g';
        }
        for (const auto& wall : walls) {
            grid[wall[0]][wall[1]] = 'w';
        }
        
        int count = 0;  
        
        for (int i = 0; i < r; ++i) {
            // Right 
            int j = 0;
            while (j < c) {
                if (grid[i][j] == 'g') {
                    ++j;
                    while (j < c && grid[i][j] != 'w' && grid[i][j] != 'g') {
                        if (grid[i][j] == '1') {
                            ++j;
                            continue;
                        }
                        grid[i][j] = '1';
                        ++count;
                        ++j;
                    }
                } else {
                    ++j;
                }
            }
            
            // Left 
            j = c - 1;
            while (j >= 0) {
                if (grid[i][j] == 'g') {
                    --j;
                    while (j >= 0 && grid[i][j] != 'w' && grid[i][j] != 'g') {
                        if (grid[i][j] == '1') {
                            --j;
                            continue;
                        }
                        grid[i][j] = '1';
                        ++count;
                        --j;
                    }
                } else {
                    --j;
                }
            }
        }

        for (int j = 0; j < c; ++j) {
            // Down 
            int i = 0;
            while (i < r) {
                if (grid[i][j] == 'g') {
                    ++i;
                    while (i < r && grid[i][j] != 'w' && grid[i][j] != 'g') {
                        if (grid[i][j] == '1') {
                            ++i;
                            continue;
                        }
                        grid[i][j] = '1';
                        ++count;
                        ++i;
                    }
                } else {
                    ++i;
                }
            }

            // Up 
            i = r - 1;
            while (i >= 0) {
                if (grid[i][j] == 'g') {
                    --i;
                    while (i >= 0 && grid[i][j] != 'w' && grid[i][j] != 'g') {
                        if (grid[i][j] == '1') {
                            --i;
                            continue;
                        }
                        grid[i][j] = '1';
                        ++count;
                        --i;
                    }
                } else {
                    --i;
                }
            }
        }

        int res = (r * c) - (count + guards.size() + walls.size());
        
        return res;
    }
};
