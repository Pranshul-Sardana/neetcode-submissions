class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Convert to a subtraction problem
        
        #Create placeholders for the number of steps required for amounts
        steps = [math.inf]*(amount+1)
        #Define the base case of amount=0
        steps[0] = 0
        
        #Iterate for each amount
        #Iterate for each coin
        #If the coin selections is valid (a-c>0)
        #Calculate steps[a] = min(steps[a],1+steps[a-c])
        for a in range(amount+1):
            for c in coins:
                if a-c >= 0:
                    steps[a] = min(steps[a],1+steps[a-c])


        #Return the coins if a possible amount exists, else -1
        return steps[a] if steps[a] < math.inf else -1


         