import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Initiate the pointer
        l, r = 1, max(piles)
        #Initiate minimum
        k_min = r

        #Iterate
        while l <= r:
            #Get center ptr
            k = l + (r-l)//2 #(l+r)//2 #
            #Initiate hours
            hrs = 0
            #Iterate for every item
            for item in piles:
                #Add time to the initiate hours
                hrs += math.ceil(item/k)
            
            #If taking too much time, move the left pointer
            if hrs > h:
                l = k + 1
            #Else move the right pointer
            else:
                r = k - 1
                k_min = min(k_min, k)

        return k_min