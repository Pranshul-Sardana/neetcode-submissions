class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        #Initiate seen set, res length, and pointers
        seen = set()
        max_res = 0
        l, r = 0, 0
        
        #Iterate while right pointer < length of s
        #If element in seen set: remove from set, reduce count, and move left ptr
        #else: add to set, increase count, and move right pointer
        while r < len(s):
            #print(f"{seen = }")
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1 
            
            max_res = max(max_res, len(seen))
            
        #Return res length
        return max_res