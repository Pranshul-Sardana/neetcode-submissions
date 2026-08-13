class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Initiate my pointer
        l, r = 0, len(nums) -1

        #Iterate till my left pointer is less than or equal to the right pointer
        while l <= r:
            #Sample to element at the middle value
            c = l + (r-l)//2
            #If element < target, move the left pointer to sample the right side
            if nums[c] < target:
                l = c + 1

            #Elif element > target, move the right pointer to sample the left side
            elif nums[c] > target:
                r = c - 1

            #else they are equal, return the element index
            else:
                return c

        #If element does not exist, return -1
        return -1