class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## Bottom up DP ##

        curr, prev = cost[-2], cost[-1]

        for item in cost[:-2][::-1]:
            temp = curr
            #print(item)
            curr = item + min(curr, prev)
            prev = temp

        return min(curr, prev)