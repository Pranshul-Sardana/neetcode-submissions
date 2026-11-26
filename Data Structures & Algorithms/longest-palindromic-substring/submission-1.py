class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #Track string and length
        max_len = 0
        string = ""

        for i in range(len(s)):
            
            for l, r in [(i,i), (i,i+1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > max_len:
                        string = s[l:r+1]
                        max_len = r-l+1

                    l -= 1
                    r += 1

        return string