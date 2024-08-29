class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]

        heights.sort(reverse=True)

        out = []
        for n in heights:
            out.append(people[n])
        
        return out