class Solution:
    def longestPalindrome(self, s: str) -> str:

        #Track longest string
        lon = ""
        
        # iterate over each element (call it center)
        for i in range(len(s)):
            # Use 2 pointers (initiate at center and move outwards)
            # Even and odd centers are different. Iterate

            for l,r in [(i,i), (i, i+1)]:
            #l, r = i,i 
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    # Check if char at indices match and r-l+1 > len(longest)
                    if r-l+1 > len(lon):
                        lon = s[l:r+1]

                    l -= 1
                    r += 1

        # Return the longest
        return lon
        
