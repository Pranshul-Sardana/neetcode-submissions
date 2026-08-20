class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Check length
        if len(s1) > len(s2):
            return False

        #Convert S1 to freq map
        #Initate a zero array with length 26 (for both s1 and s2)
        s1_list = [0]*26
        s2_list = [0]*26
        #For each item, increase the value at index (a == index 0)
        for i in range(len(s1)):
            s1_list[ord(s1[i]) - ord('a')] += 1
            s2_list[ord(s2[i]) - ord('a')] += 1
        

        #Implement sliding window for s2 and check for permutation
        #Initiate pointers
        l, r = 0, len(s1)-1
        #Start loops
        while r < len(s2):
            #If not equal
            if s1_list != s2_list:
                #Move pointers
                #Update s2_list
                s2_list[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
                r += 1
                if r < len(s2):
                    s2_list[ord(s2[r]) - ord('a')] += 1
            #else we found it
            else:
                return True

        #If never found, return false
        return False