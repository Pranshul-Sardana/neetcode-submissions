class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nested_anagram_list = []

        while len(strs) > 0:
            item = strs[0]
            anagram_list = [item]
            #print(anagram_list)
            strs.remove(item)

            remaining_strs = strs.copy()
            for item2 in strs:
                #print("1:", item2, strs)
                anagram_bool = self.isAnagram(item, item2)

                if anagram_bool:
                    anagram_list.append(item2)
                    remaining_strs.remove(item2)
                #print("2:", item2, remaining_strs)
            
            strs = remaining_strs

            nested_anagram_list.append(anagram_list)
                

        return nested_anagram_list
                
    def isAnagram(self, item: str, item2: str) -> bool:

        # If lengths of items are not equal, they can't be anagrams
        if len(item2) != len(item):
            return False

        # If the word count is not equal, then they can't be anagrams
        item_dict = {}
        item2_dict = {}
        for i in range(len(item)):
            item_dict[item[i]] = item_dict.get(item[i],0) + 1
            item2_dict[item2[i]] = item2_dict.get(item2[i],0) + 1

        if item_dict != item2_dict:
            return False

        return True