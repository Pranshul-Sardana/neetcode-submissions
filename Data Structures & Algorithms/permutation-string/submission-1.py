from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Can't be a permutation if the second string is shorter
        if len(s2) < len(s1):
            return False

        #Get the S1 frequency
        s1_freq = defaultdict(int)

        for item in s1:
            s1_freq[item] += 1
        
        #Initiate pointers using minimum string length
        l = 0
        r = 0

        s2_freq = defaultdict(int)

        #Sweep over S2
        while r < len(s2):

            #Dynamically get S2 frequency
            s2_freq[s2[r]] += 1
            r += 1

            #Avoid shorter strings
            if r < len(s1):
                continue
            
            #If S2 frequency matches S1 frequency, return True
            #print(s1_freq, s2_freq)
            if s2_freq == s1_freq:
                return True

            #Decrement the count
            s2_freq[s2[l]] -= 1
            #Remove the left pointer element from frequncy
            if s2_freq[s2[l]] == 0:
                s2_freq.pop(s2[l])
            #Increment the left pointer
            l += 1

        #If frequency never matches, return False
        return False