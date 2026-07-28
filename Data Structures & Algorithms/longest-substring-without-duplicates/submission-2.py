class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Initiate pointers
        l = 0
        substring_set = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l+=1

            substring_set.add(s[r])
            #print(f"{ len(substring_set) = }, {max_length = }")
            max_length = max(len(substring_set), max_length)

        return max_length

        



