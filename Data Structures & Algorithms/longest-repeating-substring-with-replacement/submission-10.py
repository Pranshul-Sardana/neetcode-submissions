class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Set up a hashmap for frequency
        window_frequency = defaultdict(int)
        
        # Initiate pointers and max_length 
        l = 0
        max_length = 0

        for r in range(len(s)):
            #Increase the value frequency based on where the right pointer is
            window_frequency[s[r]] += 1

            #While replacements required are more than allowed, keep on moving the left pointer
            #and keep updating the frequency
            while (r-l+1) - max(window_frequency.values()) > k:
                window_frequency[s[l]] -= 1
                l += 1

            #Get the current max length 
            max_length = max(max_length, r-l+1)

        return max_length