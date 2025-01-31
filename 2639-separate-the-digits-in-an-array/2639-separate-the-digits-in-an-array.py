class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        st = []
        for i in range(len(nums)):
            for j in str(nums[i]):
                st.append(int(j))
        return st