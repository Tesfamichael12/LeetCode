#include <vector>
using namespace std;

class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int row, col;
        // Find the location of the Rook
        for (int i = 0; i < 8; ++i) {
            for (int j = 0; j < 8; ++j) {
                if (board[i][j] == 'R') {
                    row = i;
                    col = j;
                    break;
                }
            }
        }
        
        int count = 0;
        int i, j;
        // Search upward (north) for pawns to capture
        i = row, j = col;
        while (i > 0) {
            i--;
            if (board[i][j] == 'B') break; 
            if (board[i][j] == 'p') {
                count++;
                break; 
            }
        }

        // Search downward (south) for pawns to capture
        i = row, j = col;
        while (i < 7) {
            i++;
            if (board[i][j] == 'B') break; 
            if (board[i][j] == 'p') {
                count++;
                break; 
            }
        }

        // Search leftward (west) for pawns to capture
        i = row, j = col;
        while (j > 0) {
            j--;
            if (board[i][j] == 'B') break; 
            if (board[i][j] == 'p') {
                count++;
                break; 
            }
        }

        // Search rightward (east) for pawns to capture
        i = row, j = col;
        while (j < 7) {
            j++;
            if (board[i][j] == 'B') break; 
            if (board[i][j] == 'p') {
                count++;
                break; 
            }
        }
        return count;
    }
};
