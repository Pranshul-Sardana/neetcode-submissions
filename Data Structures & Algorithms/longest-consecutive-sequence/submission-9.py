class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Initate seen set and max_length
        seen = set(nums)
        max_l = 0

        #Iterate
        for item in nums:
            if item - 1 not in seen:
                #Initiate curr length
                curr_l = 0

                #while n-length exists in set, increment current length
                #update max length
                while item + curr_l in seen:
                    curr_l += 1

                max_l = max(max_l, curr_l)
        
        #Return
        return max_l