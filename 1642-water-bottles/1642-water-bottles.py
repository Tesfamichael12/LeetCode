class Solution:
    def numWaterBottles(self, num: int, ex: int) -> int:
        totla = 0
        count = num

        while num >= ex:
            temp = num // ex
            print(temp)
            num = temp + num % ex
            count += temp

        return count 