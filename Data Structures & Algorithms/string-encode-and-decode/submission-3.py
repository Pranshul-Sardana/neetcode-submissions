class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        #Adding encoding
        for item in strs:
            encoded_str += str(len(item))+'#'+item
            
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            #Keep on iterating 
            while str(s[j]) != '#':
                j += 1
           
            length = int(s[i:j])
            # The length of the string is the current 
            res.append(s[j+1:j+1+length])
            i = j+1+length

        return res
