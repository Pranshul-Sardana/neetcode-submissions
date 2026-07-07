class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        strsWordCount = self.wordCount(strs)
        
        nested_anagram_list = []

        for item in strsWordCount:
            anagram_list = []
            
            for i, item2 in enumerate(strsWordCount):
                if item == item2:
                    anagram_list.append(strs[i])
                    
            if anagram_list not in nested_anagram_list:
                nested_anagram_list.append(anagram_list)
    
        return nested_anagram_list
            


    def wordCount(self, strs) -> []:
        countList = []
        
        for item in strs:
            item_dict = {}
            
            for word in item:
                item_dict[word] = item_dict.get(word, 0) + 1
            
            countList.append(item_dict)
        
        return countList