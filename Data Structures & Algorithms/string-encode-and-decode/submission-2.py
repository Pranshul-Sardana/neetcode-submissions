class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        #Adding encoding
        for item in strs:
            encoded_str = encoded_str+item+'..'
            
        return encoded_str

    def decode(self, s: str) -> List[str]:
        return s.split('..')[:-1]
