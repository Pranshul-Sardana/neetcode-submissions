from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Check Lengths
        if len(s) != len(t):
            return False

        #Initate Dict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        #Get Frequency count
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        #Compare freqeuncy counts
        if s_dict != t_dict:
            return False

        return True