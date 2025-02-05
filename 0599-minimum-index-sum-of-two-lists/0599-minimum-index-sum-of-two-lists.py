class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        list_1 = {}
        list_2 = {}
        res = []

        for i, word in enumerate(list1):
            if word not in list_1:
                list_1[word] = i
        for i, word in enumerate(list2):
            if word not in list_2:
                list_2[word] = i
            
        for word in list_1:
            if word in list_2:
                sum = list_1[word] + list_2[word]
                min_sum = min(min_sum, sum)
        
        for word in list_1:
            if word in list_2 and list_1[word] + list_2[word] == min_sum:
                res.append(word)

        return res

