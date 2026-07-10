class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        # Create a frequency hashmap
        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1

        
        count = [[] for _ in range(len(nums)+1)]
        for key, v  in nums_dict.items():
            count[v].append(key)
        print(f"{count = }")
                    
        topk = []
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                topk.append(n)
                #print(n, topk)
                if len(topk) == k:
                    return topk
                    #print(topk)
                    