class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Get a super multiple
        out_arr = [1]*len(nums)

        # The prefix of the left-most number is 1
        #So, starting with the second number
        prefix = 1
        for i in range(len(nums)):
            #Every number in the prefix array is the multiple of the last prefix number and the item before it
            out_arr[i] = prefix
            prefix *= nums[i]
        print(out_arr)
        
        #The postfix of the rightmost number is 1
        out_arr[-1] *= 1

        #Running the for loop in reverse
        #len(arr) - 1 points to the last element, which we have already updated
        #now, we want to update the second last element (so len(arr)-2), and we need the third last element(len(arr)-3)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            out_arr[i] *= postfix
            postfix *= nums[i]

        return out_arr