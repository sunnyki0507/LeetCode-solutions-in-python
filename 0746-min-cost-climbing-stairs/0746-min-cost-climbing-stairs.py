class Solution(object):
    def minCostClimbingStairs(self, cost):
        curr = 0
        First = cost[0]
        Second = cost[1]
        length = len(cost)
        if length <= 2:
            return min(First, Second)
        for i in range(2, length):
            curr = min(First, Second) + cost[i]
            First = Second
            Second = curr
        return min(First, Second)

        """
        :type cost: List[int]
        :rtype: int
        """
        