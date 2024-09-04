class Solution {
public:
    long long smallestNumber(long long num) {
        vector<long long> digits;
        bool isneg = num < 0;
        num = abs(num);
        
        while (num) {
            long long digit = num % 10;
            digits.push_back(digit);
            num /= 10;
        }
        
        if (isneg) {
            sort(digits.rbegin(), digits.rend()); 
        } else {
            sort(digits.begin(), digits.end()); 
            if (digits.size() > 1 && digits[0] == 0) {
                long long l = 0, r = 0;
                while (r < digits.size()) {
                    if (digits[r] != 0) {
                        swap(digits[l], digits[r]);
                        break;
                    }
                    r++;
                }
            }
        }

        long long number = 0;
        for (long long digit : digits) {
            number = number * 10 + digit;
        }
        
        return isneg ? -number : number;
    }
};
