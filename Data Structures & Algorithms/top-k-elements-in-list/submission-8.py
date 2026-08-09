from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Get freuencies
        frequencies = defaultdict(int)

        for item in nums:
            frequencies[item] += 1
        
        #Pair all elements with the same frequencies together
        paired_elemets = [[] for _ in range(len(nums)+1)]
        for num, freq in frequencies.items():
            paired_elemets[freq].append(num)
        
        #print(paired_elemets)

        #Iterate starting from the highest frequencies
        k_most_freq = []
        for val in paired_elemets[::-1]:
            for item in val:
                k_most_freq.append(item)
                if len(k_most_freq) == k:
                    return k_most_freq


