class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #print(s1)
        #Check length
        if len(s1) > len(s2):
            return False
        
        #Convert strings to frequencies
        s1_list, s2_list = [0]*26, [0]*26
        
        for i in range(len(s1)):
            s1_list[ord(s1[i])-ord('a')] += 1
            s2_list[ord(s2[i])-ord('a')] += 1

        #Create a logic to check matches
        matches = 0
        for i in range(26):
            matches += (1 if s1_list[i]==s2_list[i] else 0)
        
        #Sliding window and update matches
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            #print(r, matches)

            #Adding the right pointer
            index = ord(s2[r])-ord('a')
            s2_list[index] += 1
            if s2_list[index] == s1_list[index]:
                matches += 1
            elif s2_list[index] == s1_list[index] + 1:
                matches -= 1
            #print(s2[r], s2_list[index], s1_list[index], matches)

            #Removing the left pointer
            index = ord(s2[l])-ord('a')
            s2_list[index] -= 1
            if s2_list[index] == s1_list[index]:
                matches += 1
            elif s2_list[index] == s1_list[index] - 1:
                matches -= 1
            #print(s2[r], s2_list[index], s1_list[index], matches)
            l += 1

        
        return (True if matches == 26 else False)
