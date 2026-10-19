class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        #Initiate seen set, res length, and pointers
        seen = set()
        max_res, res = 0, 0
        l, r = 0, 0
        
        #Iterate while right pointer < length of s
        #If element in seen set: remove from set, reduce count, and move left ptr
        #else: add to set, increase count, and move right pointer
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res += 1
                r += 1
            else:
                seen.remove(s[l])
                res -= 1
                l += 1
            
            max_res = max(max_res, res)
            
        #Return res length
        return max_res