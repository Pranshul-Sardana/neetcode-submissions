class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Can't be a permutation if the second string is shorter
        if len(s2) < len(s1):
            return False

        #Create the initial arrays that contain frequency for all a-z
        #Each index represents ord(character) - ord('a')
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1 #Updating only the equal length
        
        #Create the initial matches
        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        #Setting up pointers
        #iterate through the second string
        l = 0
        for r in range(len(s1), len(s2)):
            
            if matches == 26:
                return True

            index = ord(s2[r])-ord('a')
            s2_count[index] += 1 
            #If by adding the index value at s2_count we made it equal, increment matches by 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            #If by adding the value we removed that equality, reduce the match by 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            
            l += 1

        return matches == 26