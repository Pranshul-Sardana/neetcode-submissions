class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Get a super multiple
        superMultiple = 1
        for item in nums:
            superMultiple *= item

        #Finding individual elements
        out = []
        for i in range(len(nums)):
            item = nums[i]

            #If item is 0, find the multiple of rest
            #Else, use super multiple
            if item == 0:
                nums_short = nums.copy()
                nums_short.pop(i)
                multiple = 1
                for item2 in nums_short:
                    multiple *= item2
                out.append(multiple)
            else:
                out.append(superMultiple//item)

        return out