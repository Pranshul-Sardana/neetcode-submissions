class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        sorted_dict = defaultdict(list)
        
        for item in strs:
            item_sorted = "".join(sorted(item))
            sorted_dict[item_sorted].append(item)

        return list(sorted_dict.values())