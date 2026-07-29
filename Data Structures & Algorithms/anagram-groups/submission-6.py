from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        paired_strs = defaultdict(list)

        for item in strs:
            item_sorted = "".join(sorted(item))
            paired_strs[item_sorted].append(item)

        return list(paired_strs.values())


            

            


        