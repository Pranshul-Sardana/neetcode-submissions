class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #2 Pointers
        l, r = 0, len(nums) - 1

        #Keep iterating 
        while l <= r:
            #If middle sample > target
            m = (l+r)//2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #Left sorted portion
                if target >= nums[m] or target < nums[l]: #Search right
                    l = m + 1
                else:
                    r = m - 1
            
            else: #Right sorted portion
                if target > nums[r] or target < nums[m]: #Search left
                    r = m - 1
                else:
                    l = m + 1
                    
        return -1

