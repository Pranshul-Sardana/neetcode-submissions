from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        #Get frequency map
        for item in nums:
            freq_dict[item] += 1

        #Create a 2 stage nested list (Buckets)
        #Each inner list contains all the elements that have the frequency equal to the index
        buckets = [[] for _ in range(len(nums)+1)]
        for key, v in freq_dict.items():
            buckets[v].append(key)
        #print(buckets)

        #Iterate through the buckets in reverse and get the topk elements
        topk = []
        for lists in buckets[::-1]:
            for item in lists:
                topk.append(item)
                #print(f'{item = }, {topk = }, {len(topk) = }, {k = }')
                if len(topk) == k:
                    return topk
