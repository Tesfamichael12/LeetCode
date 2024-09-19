class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = R = 0
        maxlength = 0
        hashset = set()
        while R < len(s):
            if len(s) == 1:
                maxlength = 1
            if s[R] in hashset: 
                maxlength = max(maxlength, len(hashset))
                while not(s[L] == s[R]): #if they are equal we need to move L only one step so the code outside the loop will be excuted L += 1 
                    hashset.remove(s[L])
                    L += 1
                hashset.remove(s[L])
                L += 1 # if s[R] in hashset then we can move the pointer L all the way to i + 1 where i is the index of the first occurance of s[R]
            else:
                hashset.add(s[R])
                maxlength = max(maxlength, len(hashset))
                R += 1
        return maxlength
        