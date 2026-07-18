class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase
        s = s.lower()

        #Remove special characters
        s_non_special = ""
        for char in s:
            if char.isalnum():
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