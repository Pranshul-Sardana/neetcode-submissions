class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## Bottom-up DP ##
        
        #Get the cost of last 2 steps
        prev, curr = cost[-1], cost[-2]
        #print(prev, curr)

        #Keep iterating backwards with minimum cost
        for item in cost[:-2][::-1]:
            #print(f"{item}, {curr = }, {prev = }")
            temp = curr
            curr = item + min(curr, prev)
            prev = temp
            
        #Return the minimum of 0 and 1
        return min(curr, prev)