class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Initiate pointers
        l, r = 0, len(nums) - 1

        #Search for target
        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            #Look at the left pointer and the middle pointer to guess which part of the trend we are in
            #Based on the left or right trend, write the logic
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        #If target not found, return -1
        return -1