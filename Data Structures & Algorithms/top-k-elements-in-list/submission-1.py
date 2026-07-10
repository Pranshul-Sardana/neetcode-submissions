class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1
        
        #Sorting the dictionary
        nums_dict = dict(sorted(nums_dict.items(), key=lambda x: x[1], reverse=True))
        #print(nums_dict)

        return list(nums_dict)[:k]