class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums = sorted(nums)
        for i, item in enumerate(nums):
            item_to_compare = item
            nums_short = nums[i+1:]
            #print(nums_short)
            
            if item in nums_short:
                return(True)
        return(False)
        