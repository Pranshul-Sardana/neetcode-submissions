class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Initiate a placeholder output array
        output = [1]*(len(nums))

        #Iterate over the indices
        prefix = 1
        for i in range(len(nums)):
            #Update Outs
            output[i] = prefix
            #Update prefix
            prefix *= nums[i]
            

        postfix = 1
        #Reverse iterate over the indices
        for i in range(len(nums)-1,-1,-1):
            #Update output
            output[i] *= postfix
            #Update postfix
            postfix *= nums[i]
            
            
        #Return the output
        return output
