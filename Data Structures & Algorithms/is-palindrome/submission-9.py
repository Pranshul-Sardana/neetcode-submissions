class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Initiate out pointers
        l, r = 0, len(s) - 1

        #Iterate through the string
        while l < r:
            #Only check alpha numerical
            while not (ord("a") <= ord(s[l]) <= ord("z") or 
            ord("A") <= ord(s[l]) <= ord("Z") or
            ord("0") <= ord(s[l]) <= ord("9")
            ) and l < r:
                l += 1

            while not (ord("a") <= ord(s[r]) <= ord("z") or 
            ord("A") <= ord(s[r]) <= ord("Z") or
            ord("0") <= ord(s[r]) <= ord("9")
            ) and l < r:
                r -= 1
            
            left_char = s[l]
            right_char = s[r]
            
            #Ignore case and check equality
            if left_char.lower() != right_char.lower():
                return False

            #Increment Pointers
            l += 1
            r -= 1

        return True
            