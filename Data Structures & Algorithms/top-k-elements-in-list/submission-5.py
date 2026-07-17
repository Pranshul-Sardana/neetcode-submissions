from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = Counter(nums)
        freq_nums = dict(sorted(freq_nums.items(), key=lambda x: x[1], reverse=True))

        return [list(freq_nums.keys())[i] for i in range(k)]