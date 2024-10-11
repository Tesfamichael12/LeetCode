class Solution {
public:
    int minimumRecolors(std::string blocks, int k) {
        int L = 0, numWhites = 0; 
        int minRecolors = blocks.size(); 

        for (int R = 0; R < blocks.size(); ++R) {
            if (blocks[R] == 'W') {
                numWhites++; 
            }

            
            if (R >= k - 1) {
                minRecolors = std::min(minRecolors, numWhites); 

                if (blocks[L] == 'W') {
                    numWhites--; 
                }
                L++; 
            }
        }

        return minRecolors; 
    }
};