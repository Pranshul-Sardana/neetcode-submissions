class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase
        s = s.lower()

        #Remove special characters
        s_non_special = ""
        for char in s:
            if (ord(char) in range(ord("a"),ord("z")) or (ord(char) in range(ord("A"),ord("Z")))) or (ord(char) in range(ord("0"),ord("9"))):
                s_non_special += char
        
        # Initiate 2-pointers
        left, right = 0, len(s_non_special) - 1

        #Check if the characters are unequal
        while left <= right:
            if s_non_special[left] != s_non_special[right]:
                return False
            left += 1
            right -= 1
        
        return True