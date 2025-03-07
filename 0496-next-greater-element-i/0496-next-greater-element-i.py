class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums2)

        i = len(nums2) - 1
        while i >= 0:
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]
            
            stack.append(nums2[i])
            i -= 1
        ans = []
        for n in nums1:
            ans.append(res[nums2.index(n)])
        
        return ans