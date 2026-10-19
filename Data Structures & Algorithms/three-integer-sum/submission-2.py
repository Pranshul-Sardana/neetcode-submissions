class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Initiate Empty
        ret = []
        
        #Sort
        nums.sort()

        #Loop over the first, and apply 2 pointer to the remaining
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == nums[i] * (-1):
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] < nums[i] * (-1):
                    j += 1
                else:
                    k -= 1
        
        
        #Return
        return ret