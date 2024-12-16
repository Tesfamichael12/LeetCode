class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if people[0] == limit:
            return len(people)
        
        boat_count = 0
        r = len(people) - 1
        l = 0
        while l <= r:
            if people[r] == limit:
                boat_count += 1
                r -= 1
            elif people[r] + people[l] > limit:
                boat_count += 1
                r -= 1
            else:
                boat_count += 1
                l += 1
                r -= 1
        return boat_count
