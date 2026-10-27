class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make the nums a set
        #Initiate a global longest count
        nums = set(nums)
        longest = 0

        #Iterate with every element
        for item in nums:
            #Skip if n-1 exists
            if item - 1 in nums:
                continue
            
            #initiate a local_count
            local_count = 1

            #while n + local_count exists, increase the local count
            while item + local_count in nums:
                local_count += 1
            
            #Find max
            longest = max(longest, local_count)

        #Return
        return longest