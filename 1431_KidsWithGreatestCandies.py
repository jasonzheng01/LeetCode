class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        lst = [x + extraCandies >= maxCandies for x in candies]
        return lst
