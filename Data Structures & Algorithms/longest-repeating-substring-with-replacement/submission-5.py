class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initiate pointers and max_length 
        l, r = 0, 0
        max_length = 1

        #Set up a hashmap for frequency
        window_frequency = defaultdict(int)
        
        #Set up iterations
        while r < len(s):
            #Get window frequency
            window_frequency[s[r]] += 1

            #Get length of elements except top element (replacement count)
            #Get top count and remove it with window length
            replacements_required = (r-l+1) - max(window_frequency.values())

            #If replacement count <= k, move right pointer
            if replacements_required <= k:
                #Update max_length if the current substring length > max_length
                max_length = max((r-l+1), max_length)
                r += 1
                
            #Else, move the left pointer till we remove the non-top element
            else:
                window_frequency[s[l]] -= 1
                l += 1
                r += 1

        return max_length