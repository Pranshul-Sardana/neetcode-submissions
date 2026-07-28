class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #If length of string is less than 2
        if len(s) < 2:
            return len(s)

        #Initiate pointers
        l, r = 0, 1
        substring_set = set(s[0:2])
        max_length = len(substring_set)

        while r < len(s) - 1:
            #Increase the right pointer
            r += 1

            #Check if the element is new
            if s[r] not in substring_set:
                substring_set.add(s[r])
                if len(substring_set) > max_length:
                    max_length += 1
            else:
                while s[l] != s[r]:
                        l += 1
                print(s[l], s[r])
                l += 1
                #r += 1
                substring_set = set(s[l:r+1])

        return max_length

        



