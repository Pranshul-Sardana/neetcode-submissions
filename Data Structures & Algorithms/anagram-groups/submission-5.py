class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        grouped_anagram = defaultdict(list)

        for item in strs:
            sorted_item = "".join(sorted(item))
            grouped_anagram[sorted_item].append(item)

        return list(grouped_anagram.values())