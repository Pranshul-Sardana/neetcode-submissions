class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Initiate Empty
        ret = []
        
        #Sort
        nums.sort()

        #Loop over the first, and apply 2 pointer to the remaining
        for i in range(len(nums)-2):
            j, k = i+1, len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == nums[i] * (-1):
                    #If match found, check before appending
                    if [nums[i], nums[j], nums[k]] not in ret:
                        ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif nums[j] + nums[k] < nums[i] * (-1):
                    j += 1
                else:
                    k -= 1
        
        
        #Return
        return ret