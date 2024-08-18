class Solution(object):
    def isPalindrome(self, x):

        # uisng simple sytax sugar in python
        x = str(x)
        return x == x[::-1] #In Python, slicing notation x[start:stop:step] allows us to extract a portion of the sequence x based on the given parameters.