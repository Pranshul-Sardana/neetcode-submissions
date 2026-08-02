from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        #Get frequency map
        for item in nums:
            freq_dict[item] += 1

        #Sort by values
        freq_dict = sorted(freq_dict, key=lambda x:freq_dict[x], 
        reverse=True)

        return freq_dict[:k]