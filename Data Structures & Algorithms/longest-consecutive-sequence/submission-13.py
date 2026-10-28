class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Make it a set
        #Initiate global length
        nums = set(nums)
        max_l = 0

        #Iterate each element
        for n in nums:
            #If n-1 exists, skip it
            if n - 1 in nums:
                continue
            
            #Initiate local length
            curr_l = 1
            #While n+local_length exists
                #increase local length
            while n + curr_l in nums:
                curr_l += 1

            #Get max
            max_l = max(max_l, curr_l)

        #Return max
        return max_l