class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding window
        
        #Initiate ptrs
        l, r = 0, 0
        #Track max length (Initiate) and seen
        max_l = 0
        seen = set()

        #Iterate: while r < len(s)
        #While element seen before, keep removing duplicates and incrementing left ptr
        # Add the element, increment right pointer, and update max length
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r+=1
            max_l = max(max_l, len(seen))

        #Return max length
        return max_l


