class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for item in strs:
            encoded_str += f"{len(item)}#{item}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        out_list = []
        
        l = 0

        while l < len(s):
            r = l

            while s[r] != '#':
                r += 1

            string_length = int(s[l:r])
            
            word = s[r+1:r+1+string_length]
            
            #Appending the word to list
            out_list.append(word)

            #Moving the pointers
            l = r+1+string_length

        return out_list

