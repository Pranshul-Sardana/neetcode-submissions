class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        
        for i in range(len(nums)):
            out.append(1) #Assign the i_th element as 1
            
            for j in range(len(nums)):
                if i == j: #Skip self
                    continue
                out[i]*= nums[j] #Multiply the numbers

        return out