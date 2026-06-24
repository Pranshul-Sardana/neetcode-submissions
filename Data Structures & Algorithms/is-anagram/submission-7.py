class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = sorted(s)
        t_list = sorted(t)
        
        #print(f"{s_dict = }")
        #print(f"{t_dict = }")
        if s_list == t_list:
            return True
        else:
            return False
        