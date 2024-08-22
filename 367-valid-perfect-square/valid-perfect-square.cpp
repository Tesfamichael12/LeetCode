class Solution {
public:
    bool isPerfectSquare(int num) {
         return pow(num, 0.5) ==  (int) pow(num, 0.5);
    }
};